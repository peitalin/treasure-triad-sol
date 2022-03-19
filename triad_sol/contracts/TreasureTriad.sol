
//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.0;

import "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "hardhat/console.sol";

import "./TreasureTriadCardStats.sol";
import "./ShittyRandom.sol";
import { TreasureTriadCardStats, CardStats } from "./TreasureTriadCardStats.sol";


struct TreasureCard {
    string tcard;
    // string tokenId;
    Player player;
}

enum Player {
    nature,
    none,
    range,
    fighter,
    spellcaster,
    seige,
    assassin,
    riverman,
    numeraire,
    common
}
// nature => contract
// user => msg.sender



contract TreasureTriad is Initializable {

    TreasureTriadCardStats public ttCardStats = new TreasureTriadCardStats();
    ShittyRandom public shittyRandom = new ShittyRandom();

    mapping(uint => mapping(uint => TreasureCard)) public grid;
    event NaturesInitialCells(uint8[2][]);

    address owner;
    uint public gridRows;
    uint public gridCols;
    int public convertedCards;
    TreasureCard noneCard;


    function initialize(uint _gridSize) public initializer {

        require(2 < _gridSize && _gridSize < 5, "grid size must be 3x3 or 4x4");

        owner = msg.sender;
        gridRows = _gridSize;
        gridCols = _gridSize;
        noneCard = TreasureCard({ tcard: "", player: Player.none });

        // initiate grid with empty cards
        for (uint i = 0; i < gridCols; i++) {
            for (uint j = 0; j < gridRows; j++) {
                TreasureCard memory t = noneCard;
                grid[i][j] = t;
            }
        }
        // start by letting Nature place N cards randomly on the grid
        // naturePlacesInitialCards(3);
    }

    modifier withinGrid(uint _row, uint _col) {
        // gridRows and gridCols are lengths, not indexes
        // e.g. 3x3 grid => gridRows and gridCols is 3
        require(_row >= 0 && _row < gridRows, "row must be within 0...gridRows");
        require(_col >= 0 && _col < gridCols, "col must be within 0...gridCols");
        _;
    }

    modifier isEmptyCell(uint _row, uint _col) {
        require(_isEmptyCell(_row, _col), "Cell Occupied");
        _;
    }

    function _isEmptyCell(uint _row, uint _col) private view returns (bool) {
        TreasureCard memory existingCard = grid[_row][_col];
        return cardExists(existingCard) ? false : true;
    }

    function cardExists(TreasureCard memory _c) private pure returns (bool) {
        return bytes(_c.tcard).length != 0;
    }

    function cardStatsExists(CardStats memory _c) private pure returns (bool) {
        return bytes(_c.name).length != 0;
    }

    function getCardStats(TreasureCard memory card) public view returns (CardStats memory) {
        return cardExists(card)
            ? ttCardStats.getCard(card)
            : ttCardStats.getCard(noneCard);
    }

    function getCardAtCell(uint _row, uint _col) public view returns (TreasureCard memory) {
        return grid[_row][_col];
    }

    function _incrementConvertedCards(int _num_flips) private returns (int) {
        convertedCards += _num_flips;
        return convertedCards;
    }

    function getConvertedCards() public view returns (int) {
        return convertedCards;
    }

    ////////////////////////////////////
    // Initializing Nature's Card Picks
    ///////////////////////////////////

    function _naturePlacesCard(uint _row, uint _col) private returns (bool) {
        if (!_isEmptyCell(_row, _col)) {
            return false;
        } else {

            // Ideally randomizer has difficulty parameters so that when difficulty is low
            // more low-tier cards are selected, and vice versa when difficulty is high
            string[] memory randCards = ttCardStats.getCardNames();
            uint randInt = shittyRandom.requestRandomNumber(_row + _col) % randCards.length;
            string memory randCard = randCards[randInt];

            grid[_row][_col] = TreasureCard({
                tcard: randCard,
                player: Player.nature
            });
            return true;
        }
    }

    function naturePlacesInitialCards(uint _number) public {

        require(msg.sender == owner, "owner only");
        uint totalCardsPlaced = 0;
        uint8[2][] memory sampledGridCells = shittyRandom.sampleRandomGridCellCoords(_number);

        uint i; // counter

        while (totalCardsPlaced < _number) {

            uint randRow = sampledGridCells[i][0];
            uint randCol = sampledGridCells[i][1];

            if (_naturePlacesCard(randRow, randCol)) {
                totalCardsPlaced++;
                i++;
            }
            if (totalCardsPlaced == _number) {
                break;
            }
        }
        emit NaturesInitialCells(sampledGridCells);
    }

    //////////////////////////////
    // Treasure Triad Logic
    //////////////////////////////

    function stakeTreasureCard(
        uint _row,
        uint _col,
        string calldata _name,
        Player _player
    ) isEmptyCell(_row, _col) withinGrid(_row, _col) public {
        TreasureCard memory c = TreasureCard(_name, _player);
        grid[_row][_col] = c;
        _tryFlipCardOnTop(_row, _col, _player, c);
        _tryFlipCardOnBottom(_row, _col, _player, c);
        _tryFlipCardOnLeft(_row, _col, _player, c);
        _tryFlipCardOnRight(_row, _col, _player, c);
    }

    // test purposes only, remove
    function stakeTreasureCardAsNature(
        uint _row,
        uint _col,
        string calldata _name
    ) isEmptyCell(_row, _col) public {
        require(address(msg.sender) == owner, "owner only");
        TreasureCard memory c = TreasureCard(_name, Player.nature);
        grid[_row][_col] = c;
        _tryFlipCardOnTop(_row, _col, Player.nature, c);
        _tryFlipCardOnBottom(_row, _col, Player.nature, c);
        _tryFlipCardOnLeft(_row, _col, Player.nature, c);
        _tryFlipCardOnRight(_row, _col, Player.nature, c);
    }

    function _tryFlipCardOnTop(
        uint _row,
        uint _col,
        Player _player,
        TreasureCard memory current_card
    ) private {
        // Try flip Card to the TOP
        if (_row >= 1) {
            // check row with -1 offset is at least 0 (within grid)
            // check for underflow issues with negative offsets

            CardStats memory current_card_stats = ttCardStats.getCard(current_card);
            TreasureCard memory card_top = grid[_row-1][_col];
            CardStats memory card_top_stats = getCardStats(card_top);

            if (cardStatsExists(card_top_stats)) {
                // compare north of current card to south of card above
                if (current_card_stats.n > card_top_stats.s) {
                    // if score on staked card is bigger, flip the card to new player
                    grid[_row-1][_col].player = _player;

                    int card_flips = (_player == Player.nature) ? int(-1) : int(1);
                    _incrementConvertedCards(card_flips);
                }
            }
        }
    }

    function _tryFlipCardOnBottom(
        uint _row,
        uint _col,
        Player _player,
        TreasureCard memory current_card
    ) private {
        // Try flip Card to the BOTTOM
        if (_row < gridRows) {
            // check row with +1 offset is less than gridRows (within grid)

            CardStats memory current_card_stats = ttCardStats.getCard(current_card);
            TreasureCard memory card_top = grid[_row+1][_col];
            CardStats memory card_top_stats = getCardStats(card_top);

            if (cardStatsExists(card_top_stats)) {
                // compare south of current card to north of card below
                if (current_card_stats.s > card_top_stats.n) {
                    grid[_row+1][_col].player = _player;

                    int card_flips = (_player == Player.nature) ? int(-1) : int(1);
                    _incrementConvertedCards(card_flips);
                }
            }
        }
    }

    function _tryFlipCardOnRight(
        uint _row,
        uint _col,
        Player _player,
        TreasureCard memory current_card
    ) private {
        // Try flip Card to the RIGHT
        if (_col < gridCols) {
            // check col with +1 offset is less than gridCols (withinGrid)

            CardStats memory current_card_stats = ttCardStats.getCard(current_card);
            TreasureCard memory card_right = grid[_row][_col+1];
            CardStats memory card_right_stats = getCardStats(card_right);

            if (cardStatsExists(card_right_stats)) {
                // compare east-side of current card to west-side of card on the right
                if (current_card_stats.e > card_right_stats.w) {
                    // if score on staked card is bigger, flip the card to new player
                    grid[_row][_col+1].player = _player;

                    int card_flips = (_player == Player.nature) ? int(-1) : int(1);
                    _incrementConvertedCards(card_flips);
                }
            }
        }
    }

    function _tryFlipCardOnLeft(
        uint _row,
        uint _col,
        Player _player,
        TreasureCard memory current_card
    ) private {
        // Try flip Card to the LEFT
        if (_col >= 1) {
            // check col with -1 offset is at least 0 (within grid)
            // check for underflow issues with negative offsets

            CardStats memory current_card_stats = ttCardStats.getCard(current_card);
            TreasureCard memory card_left = grid[_row][_col-1];
            CardStats memory card_left_stats = getCardStats(card_left);

            if (cardStatsExists(card_left_stats)) {
                // compare west-side of current card to east-side of card on the left
                if (current_card_stats.w > card_left_stats.e) {
                    grid[_row][_col-1].player = _player;

                    int card_flips = (_player == Player.nature) ? int(-1) : int(1);
                    _incrementConvertedCards(card_flips);
                }
            }
        }
    }

}


