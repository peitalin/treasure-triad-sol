
//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.0;

import "@openzeppelin/contracts-upgradeable/proxy/utils/Initializable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "hardhat/console.sol";

import "./TreasureTriadCardStats.sol";
import "./ShittyRandom.sol";
import { TreasureTriadCardStats, CardStats } from "./TreasureTriadCardStats.sol";


struct TreasureCard {
    string treasure;
    // string tokenId;
    Player player;
}

enum Player { nature, user, none }
// nature => contract
// user => msg.sender



contract TreasureTriad is Initializable {

    // import contracts
    TreasureTriadCardStats public ttCardStats = new TreasureTriadCardStats();
    ShittyRandom public shittyRandom = new ShittyRandom();

    mapping(uint => mapping(uint => TreasureCard)) public grid;

    address owner;
    uint public gridRows;
    uint public gridCols;
    TreasureCard noneCard;


    function initialize(uint _gridSize) public initializer {

        require(2 < _gridSize && _gridSize < 5, "grid size must be 3x3 or 4x4");

        owner = msg.sender;
        gridRows = _gridSize;
        gridCols = _gridSize;
        noneCard = TreasureCard({ treasure: "", player: Player.none });

        // initiate grid with empty cards
        for (uint i = 0; i < gridCols; i++) {
            for (uint j = 0; j < gridRows; j++) {
                TreasureCard memory t = TreasureCard("", Player.none);
                grid[i][j] = t;
            }
        }
        // start by letting Nature place N cards randomly on the grid
        // _naturePlacesInitialCards(3);
    }

    modifier withinGrid(uint _row, uint _col) {
        string memory rowErrMsg = string(abi.encodePacked("row must be within 0 and ", gridRows-1));
        string memory colErrMsg = string(abi.encodePacked("col must be within 0 and ", gridCols-1));
        // gridRows and gridCols are lengths, not indexes
        // e.g. 3x3 grid => gridRows and gridCols is 3
        require(_row >= 0 && _row < gridRows, rowErrMsg);
        require(_col >= 0 && _col < gridCols, colErrMsg);
        _;
    }

    modifier isEmptyCell(uint _row, uint _col) {
        string memory existingCard = grid[_row][_col].treasure;
        string memory errMsg = string(abi.encodePacked("Cell Occupied: ", existingCard));
        require(_isEmptyCell(_row, _col), errMsg);
        _;
    }

    function _isEmptyCell(uint _row, uint _col) private view returns (bool) {
        TreasureCard memory existingCard = grid[_row][_col];
        return cardExists(existingCard) ? false : true;
    }

    function cardExists(TreasureCard memory _c) private pure returns (bool) {
        return bytes(_c.treasure).length != 0;
    }

    function cardStatsExists(CardStats memory _c) private pure returns (bool) {
        return bytes(_c.name).length != 0;
    }


    function _shittyNaturePlacesCard(uint _row, uint _col, uint n) private returns (bool) {
        if (!_isEmptyCell(_row, _col)) {
            return false;
        } else {
            uint randInt = shittyRandom.requestRandomNumber(n + 11) % 3;
            string[3] memory randCards = ["grin", "honeycomb", "castle"];
            string memory randCard = randCards[randInt];
            // console.log("randCard: ", randCard);
            grid[_row][_col] = TreasureCard({
                treasure: randCard,
                player: Player.nature
            });
            return true;
        }
    }

    function _naturePlacesInitialCards(uint _number) private {

        uint totalCardsPlaced = 0;
        uint max_tries = 20;
        // we want Nature to place 3x cards
        // but there is chance Nature tries to place cards on cells
        // with pre-existing cards => error
        for (uint i = 1; i < max_tries; i++) {
            // Nature picks a random cell to place a card
            // ADD PROPER RANDOMIZER
            uint randRow1 = shittyRandom.requestRandomNumber(totalCardsPlaced + 11) % gridRows;
            uint randCol1 = shittyRandom.requestRandomNumber(totalCardsPlaced + 10) % gridCols;
            console.log("\nplaced: ", randRow1, randCol1);

            if (_shittyNaturePlacesCard(randRow1, randCol1, totalCardsPlaced)) {
                totalCardsPlaced++;
            }
            console.log("totalCardsPlaced: ", totalCardsPlaced);
            if (totalCardsPlaced == _number) {
                break;
            }
        }
    }

    function getCardAtCell(uint _row, uint _col) public view returns (TreasureCard memory) {
        TreasureCard memory t = grid[_row][_col];
        return t;
    }

    function stakeTreasureCard(
        uint _row,
        uint _col,
        string calldata _name
    ) isEmptyCell(_row, _col) withinGrid(_row, _col) public {
        TreasureCard memory c = TreasureCard(_name, Player.user);
        grid[_row][_col] = c;
        tryFlipCardOnTop(_row, _col, Player.user, c);
        tryFlipCardOnBottom(_row, _col, Player.user, c);
        tryFlipCardOnLeft(_row, _col, Player.user, c);
        tryFlipCardOnRight(_row, _col, Player.user, c);
    }

    // test purposes only
    function stakeTreasureCardAsNature(
        uint _row,
        uint _col,
        string calldata _name
    ) isEmptyCell(_row, _col) public {
        require(address(msg.sender) == owner, "owner only");
        TreasureCard memory c = TreasureCard(_name, Player.nature);
        grid[_row][_col] = c;
        tryFlipCardOnTop(_row, _col, Player.nature, c);
        tryFlipCardOnBottom(_row, _col, Player.nature, c);
        tryFlipCardOnLeft(_row, _col, Player.nature, c);
        tryFlipCardOnRight(_row, _col, Player.nature, c);
    }


    function getCardStats(TreasureCard memory card) public view returns (CardStats memory) {
        return cardExists(card)
            ? ttCardStats.getCard(card)
            : ttCardStats.getCard(noneCard);
    }


    function tryFlipCardOnTop(
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
                }
            }
        }
    }


    function tryFlipCardOnBottom(
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
                }
            }
        }
    }

    function tryFlipCardOnRight(
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
                }
            }
        }
    }

    function tryFlipCardOnLeft(
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
                }
            }
        }
    }

}


