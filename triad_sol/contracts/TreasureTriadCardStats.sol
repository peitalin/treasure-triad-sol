//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.0;
import "hardhat/console.sol";
import { TreasureCard } from "./TreasureTriad.sol";

struct CardStats {
    uint n;
    uint e;
    uint s;
    uint w;
    uint tokenId;
    string name;
}
// north, east, south, west


contract TreasureTriadCardStats {

	mapping(string => CardStats) cards;

    constructor() {

        // Find a way to reference this data from IPFS

        cards[''] = CardStats({
            n: 0,
            e: 0,
            s: 0,
            w: 0,
            tokenId: 0,
            name: ""
        });


        cards['honeycomb'] = CardStats({
            n: 2,
            e: 8,
            s: 8,
            w: 4,
            tokenId: 97,
            name: "honeycomb"
        });

        cards['grin'] = CardStats({
            n: 8,
            e: 2,
            s: 8,
            w: 2,
            tokenId: 95,
            name: "grin"
        });

        cards['castle'] = CardStats({
            n: 3,
            e: 6,
            s: 5,
            w: 7,
            tokenId: 54,
            name: "castle"
        });

        cards['mollusk shell'] = CardStats({
            n: 1,
            e: 6,
            s: 4,
            w: 7,
            tokenId: 105,
            name: "mollusk shell"
        });

        cards['red feather'] = CardStats({
            n: 2,
            e: 7,
            s: 6,
            w: 3,
            tokenId: 132,
            name: "red feather"
        });

        cards['divine hourglass'] = CardStats({
            n: 4,
            e: 6,
            s: 2,
            w: 7,
            tokenId: 74,
            name: "diving hourglass"
        });

        cards['cow'] = CardStats({
            n: 4,
            e: 4,
            s: 7,
            w: 2,
            tokenId: 72,
            name: "cow"
        });

        cards['ox'] = CardStats({
            n: 5,
            e: 5,
            s: 4,
            w: 3,
            tokenId: 114,
            name: "ox"
        });

        cards['lumber'] = CardStats({
            n: 5,
            e: 1,
            s: 3,
            w: 5,
            tokenId: 103,
            name: "lumber"
        });

        cards['donkey'] = CardStats({
            n: 5,
            e: 5,
            s: 5,
            w: 5,
            tokenId: 76,
            name: "donkey"
        });

        cards['dragon tail'] = CardStats({
            n: 3,
            e: 5,
            s: 2,
            w: 1,
            tokenId: 77,
            name: "dragon tail"
        });

        cards['bottomless elixer'] = CardStats({
            n: 4,
            e: 2,
            s: 7,
            w: 7,
            tokenId: 51,
            name: "bottomless elixer"
        });

        cards['small bird'] = CardStats({
            n: 7,
            e: 2,
            s: 3,
            w: 5,
            tokenId: 152,
            name: "small bird"
        });

        cards['immovable stone'] = CardStats({
            n: 5,
            e: 6,
            s: 5,
            w: 6,
            tokenId: 98,
            name: "immovable stone"
        });

        cards['red feather'] = CardStats({
            n: 2,
            e: 7,
            s: 6,
            w: 3,
            tokenId: 132,
            name: "red feather"
        });
    }

    function getCard(TreasureCard calldata _card) public view returns (CardStats memory) {
        return cards[_card.treasure];
    }

    function addCard(
        string calldata _name,
        uint _n,
        uint _e,
        uint _s,
        uint _w,
        uint _tokenId
    ) public returns (CardStats memory) {

        require(cards[_name].tokenId == 0, "_name clash");

        CardStats memory newCard = CardStats({
            n: _n,
            e: _e,
            s: _s,
            w: _w,
            tokenId: _tokenId,
            name: _name
        });
        cards[_name] = newCard;
        return newCard;
    }

    function removeCard(string calldata _name) public {
        delete cards[_name];
    }

}


    // CARDS = {
    //     // T1
    //     'honeycomb': { // tokenId 97
    //         'n': 2,
    //         'e': 8,
    //         's': 8,
    //         'w': 4,
    //     },
    //     'grin': { // tokenId 95
    //         'n': 8,
    //         'e': 2,
    //         's': 8,
    //         'w': 2,
    //     },
    //     'bottomless elixer': { // tokenId 51
    //         'n': 4,
    //         'e': 2,
    //         's': 7,
    //         'w': 7,
    //     },
    //     'cap of invisibility': { // tokenId 52
    //         'n': 2,
    //         'e': 8,
    //         's': 5,
    //         'w': 3,
    //     },
    //     'ancient relic': { // tokenId 39
    //         'n': 7,
    //         'e': 7,
    //         's': 5,
    //         'w': 3,
    //     },
    //     'castle': { // tokenId 54
    //         'n': 3,
    //         'e': 6,
    //         's': 5,
    //         'w': 7,
    //     },
    //     // T2
    //     'thread of divine silk': { // tokenId 161
    //         'n': 7,
    //         'e': 5,
    //         's': 3,
    //         'w': 4,
    //     },
    //     'immovable stone': { // tokenId 98
    //         'n': 5,
    //         'e': 6,
    //         's': 5,
    //         'w': 6,
    //     },
    //     'snow white feather': { // tokenId 153
    //         'n': 6,
    //         'e': 2,
    //         's': 7,
    //         'w': 3,
    //     },
    //     'ivory breast pin': { // tokenId 99
    //         'n': 3,
    //         'e': 7,
    //         's': 3,
    //         'w': 6,
    //     },
    //     'military stipend': { // tokenId 104
    //         'n': 7,
    //         'e': 4,
    //         's': 4,
    //         'w': 4,
    //     },
    //     'bait for monsters': { // tokenId 47
    //         'n': 7,
    //         'e': 3,
    //         's': 6,
    //         'w': 1,
    //     },
    //     'mollusk shell': { // tokenId 105
    //         'n': 1,
    //         'e': 6,
    //         's': 4,
    //         'w': 7,
    //     },
    //     'red feather': { // tokenId 132
    //         'n': 2,
    //         'e': 7,
    //         's': 6,
    //         'w': 3,
    //     },
    //     'divine hourglass': { // tokenId 74
    //         'n': 4,
    //         'e': 6,
    //         's': 2,
    //         'w': 7,
    //     },
    //     'bag of mushrooms': { // tokenId 46
    //         'n': 6,
    //         'e': 5,
    //         's': 6,
    //         'w': 5,
    //     },
    //     'carriage': { // tokenId 53
    //         'n': 2,
    //         'e': 3,
    //         's': 6,
    //         'w': 7,
    //     },
    //     // T3
    //     'small bird': { // tokenId 152
    //         'n': 7,
    //         'e': 2,
    //         's': 3,
    //         'w': 5,
    //     },
    //     'unbreakable pocketwatch': { // tokenId 162
    //         'n': 6,
    //         'e': 2,
    //         's': 6,
    //         'w': 3,
    //     },
    //     'cow': { // tokenId 72
    //         'n': 4,
    //         'e': 4,
    //         's': 7,
    //         'w': 2,
    //     },
    //     'divine mask': { // tokenId 75
    //         'n': 5,
    //         'e': 6,
    //         's': 5,
    //         'w': 3,
    //     },
    //     'favor from the gods': { // tokenId 82
    //         'n': 5,
    //         'e': 6,
    //         's': 3,
    //         'w': 5,
    //     },
    //     'score of ivory': { // tokenId 99
    //         'n': 7,
    //         'e': 1,
    //         's': 5,
    //         'w': 2,
    //     },
    //     'framed butterfly': { // tokenId 91
    //         'n': 7,
    //         'e': 5,
    //         's': 3,
    //         'w': 1,
    //     },
    //     'pot of gold': { // tokenId 116
    //         'n': 4,
    //         'e': 5,
    //         's': 5,
    //         'w': 5,
    //     },
    //     'common bead': { // tokenId 68
    //         'n': 1,
    //         'e': 2,
    //         's': 6,
    //         'w': 6,
    //     },
    //     'jar of fairies': { // tokenId 100
    //         'n': 6,
    //         'e': 6,
    //         's': 3,
    //         'w': 2,
    //     },
    //     // T4
    //     'witches broom': { // tokenId 164
    //         'n': 4,
    //         'e': 4,
    //         's': 5,
    //         'w': 2,
    //     },
    //     'green rupee': { // tokenId 94
    //         'n': 5,
    //         'e': 2,
    //         's': 5,
    //         'w': 3,
    //     },
    //     'lumber': { // tokenId 103
    //         'n': 5,
    //         'e': 1,
    //         's': 3,
    //         'w': 5,
    //     },
    //     'ox': { // tokenId 114
    //         'n': 5,
    //         'e': 5,
    //         's': 4,
    //         'w': 3,
    //     },
    //     'donkey': { // tokenId 76
    //         'n': 5,
    //         'e': 5,
    //         's': 5,
    //         'w': 5,
    //     },
    //     'common feather': { // tokenId 69
    //         'n': 6,
    //         'e': 1,
    //         's': 4,
    //         'w': 3,
    //     },
    //     'grain': { // tokenId 93
    //         'n': 5,
    //         'e': 3,
    //         's': 3,
    //         'w': 4,
    //     },
    //     'common relic': { // tokenId 71
    //         'n': 6,
    //         'e': 2,
    //         's': 2,
    //         'w': 3,
    //     },
    //     'blue rupee': { // tokenId 49
    //         'n': 6,
    //         'e': 3,
    //         's': 1,
    //         'w': 3,
    //     },
    //     // T5
    //     'half penny': { // tokenId 96
    //         'n': 4,
    //         'e': 2,
    //         's': 4,
    //         'w': 3,
    //     },
    //     'diamond': { // tokenId 73
    //         'n': 2,
    //         'e': 1,
    //         's': 6,
    //         'w': 1,
    //     },
    //     'dragon tail': { // tokenId 77
    //         'n': 3,
    //         'e': 5,
    //         's': 2,
    //         'w': 1,
    //     },
    //     'gold coin': { // tokenId 92
    //         'n': 1,
    //         'e': 5,
    //         's': 4,
    //         'w': 1,
    //     },
    //     'beetle wings': { // tokenId 48
    //         'n': 2,
    //         'e': 1,
    //         's': 4,
    //         'w': 4,
    //     },
    //     'silver coin': { // tokenId 151
    //         'n': 2,
    //         'e': 3,
    //         's': 1,
    //         'w': 5,
    //     },
    //     'pearl': { // tokenId 115
    //         'n': 6,
    //         'e': 1,
    //         's': 1,
    //         'w': 2,
    //     },
    //     'red rupee': { // tokenId 133
    //         'n': 1,
    //         'e': 3,
    //         's': 3,
    //         'w': 5,
    //     },
    //     'emerald': { // tokenId 79
    //         'n': 5,
    //         'e': 1,
    //         's': 1,
    //         'w': 3,
    //     },
    //     'quarter penny': { // tokenId 117
    //         'n': 1,
    //         'e': 4,
    //         's': 1,
    //         'w': 5,
    //     },
    //     'none': {
    //         'n': ' ',
    //         'e': ' ',
    //         's': ' ',
    //         'w': ' ',
    //     },
    // }