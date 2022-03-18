

## Each legion class's skill affinities
legion_affinities = {
    "all class": [
        "alchemy",
        "arcana",
        "brewing",
        "enchanting",
        "leather working",
        "smithing",
    ],
    "range": [
        "leather working",
        "alchemy",
    ],
    "fighter": [
        "smithing",
        "enchanting",
    ],
    "spellcaster": [
        "arcana",
        "enchanting",
    ],
    "seige": [
        "alchemy",
        "smithing",
    ],
    "assassin": [
        "brewing",
        "leather working",
    ],
    "numeraire": [
        "arcana",
    ],
    "riverman": [
        "brewing",
    ],
    "common": [
    ],
}


def getAffinityBoost(current_cell_affinity, current_card_affinity, legion_class):

    affinity_boost = 0
    l_affinities = legion_affinities.get(legion_class)

    if current_cell_affinity == current_card_affinity:
        affinity_boost += 1

    if l_affinities:
        for aff in l_affinities:
            if current_cell_affinity == aff:
                affinity_boost += 1

    if affinity_boost > 0:
        print("\ncurrent_cell_affinity", current_cell_affinity)
        print("current_card_affinity", current_card_affinity)
        print("legion_class", legion_class)
        print("affinity boost: ", affinity_boost)
        print("\n")
    return affinity_boost

## Card Scores for each Treasure
# n: north
# e: east
# s: south
# w: west
CARDS = {
    'gen0_1_1': { # tokenId ??
        'n': 9,
        'e': 7,
        's': 9,
        'w': 7,
        'affinity': "legions",
    },
    'gen0_rare': { # tokenId ??
        'n': 5,
        'e': 8,
        's': 5,
        'w': 8,
        'affinity': "legions",
    },
    'gen0_uncommon': { # tokenId ??
        'n': 8,
        'e': 8,
        's': 2,
        'w': 2,
        'affinity': "legions",
    },
    'gen0_special': { # tokenId ??
        'n': 7,
        'e': 3,
        's': 8,
        'w': 5,
        'affinity': "legions",
    },
    'gen0_common': { # tokenId ??
        'n': 4,
        'e': 3,
        's': 8,
        'w': 7,
        'affinity': "legions",
    },
    # Aux Legions
    'gen1_rare': { # tokenId ??
        'n': 6,
        'e': 7,
        's': 2,
        'w': 3,
        'affinity': "legions",
    },
    'gen1_uncommon': { # tokenId ??
        'n': 4,
        'e': 2,
        's': 5,
        'w': 7,
        'affinity': "legions",
    },
    'gen1_common': { # tokenId ??
        'n': 5,
        'e': 5,
        's': 6,
        'w': 6,
        'affinity': "legions",
    },

    # T1
    'honeycomb': { # tokenId 97
        'n': 2,
        'e': 8,
        's': 8,
        'w': 4,
        'affinity': "leather working",
    },
    'grin': { # tokenId 95
        'n': 8,
        'e': 2,
        's': 8,
        'w': 2,
        'affinity': "arcana",
    },
    'bottomless elixer': { # tokenId 51
        'n': 4,
        'e': 2,
        's': 7,
        'w': 7,
        'affinity': "enchanting",
    },
    'cap of invisibility': { # tokenId 52
        'n': 2,
        'e': 8,
        's': 5,
        'w': 3,
        'affinity': "smithing",
    },
    'ancient relic': { # tokenId 39
        'n': 7,
        'e': 7,
        's': 5,
        'w': 3,
        'affinity': "brewing",
    },
    'castle': { # tokenId 54
        'n': 3,
        'e': 6,
        's': 5,
        'w': 7,
        'affinity': "alchemy",
    },
    # T2
    'thread of divine silk': { # tokenId 161
        'n': 7,
        'e': 5,
        's': 3,
        'w': 4,
        'affinity': "arcana",
    },
    'immovable stone': { # tokenId 98
        'n': 5,
        'e': 6,
        's': 5,
        'w': 6,
        'affinity': "enchanting",
    },
    'snow white feather': { # tokenId 153
        'n': 6,
        'e': 2,
        's': 7,
        'w': 3,
        'affinity': "enchanting",
    },
    'ivory breast pin': { # tokenId 99
        'n': 3,
        'e': 7,
        's': 3,
        'w': 6,
        'affinity': "alchemy",
    },
    'military stipend': { # tokenId 104
        'n': 7,
        'e': 4,
        's': 4,
        'w': 4,
        'affinity': "smithing",
    },
    'bait for monsters': { # tokenId 47
        'n': 7,
        'e': 3,
        's': 6,
        'w': 1,
        'affinity': "brewing",
    },
    'mollusk shell': { # tokenId 105
        'n': 1,
        'e': 6,
        's': 4,
        'w': 7,
        'affinity': "leather working",
    },
    'red feather': { # tokenId 132
        'n': 2,
        'e': 7,
        's': 6,
        'w': 3,
        'affinity': "brewing",
    },
    'divine hourglass': { # tokenId 74
        'n': 4,
        'e': 6,
        's': 2,
        'w': 7,
        'affinity': "arcana",
    },
    'bag of mushrooms': { # tokenId 46
        'n': 6,
        'e': 5,
        's': 6,
        'w': 5,
        'affinity': "leather working",
    },
    'carriage': { # tokenId 53
        'n': 2,
        'e': 3,
        's': 6,
        'w': 7,
        'affinity': "smithing",
    },
    # T3
    'small bird': { # tokenId 152
        'n': 7,
        'e': 2,
        's': 3,
        'w': 5,
        'affinity': "leather working",
    },
    'unbreakable pocketwatch': { # tokenId 162
        'n': 6,
        'e': 2,
        's': 6,
        'w': 3,
        'affinity': "arcana",
    },
    'cow': { # tokenId 72
        'n': 4,
        'e': 4,
        's': 7,
        'w': 2,
        'affinity': "leather working",
    },
    'divine mask': { # tokenId 75
        'n': 5,
        'e': 6,
        's': 5,
        'w': 3,
        'affinity': "arcana",
    },
    'favor from the gods': { # tokenId 82
        'n': 5,
        'e': 6,
        's': 3,
        'w': 5,
        'affinity': "brewing",
    },
    'score of ivory': { # tokenId 99
        'n': 7,
        'e': 1,
        's': 5,
        'w': 2,
        'affinity': "alchemy",
    },
    'framed butterfly': { # tokenId 91
        'n': 7,
        'e': 5,
        's': 3,
        'w': 1,
        'affinity': "enchanting",
    },
    'pot of gold': { # tokenId 116
        'n': 4,
        'e': 5,
        's': 5,
        'w': 5,
        'affinity': "smithing",
    },
    'common bead': { # tokenId 68
        'n': 1,
        'e': 2,
        's': 6,
        'w': 6,
        'affinity': "alchemy",
    },
    'jar of fairies': { # tokenId 100
        'n': 6,
        'e': 6,
        's': 3,
        'w': 2,
        'affinity': "enchanting",
    },
    # T4
    'witches broom': { # tokenId 164
        'n': 4,
        'e': 4,
        's': 5,
        'w': 2,
        'affinity': "brewing",
    },
    'green rupee': { # tokenId 94
        'n': 5,
        'e': 2,
        's': 5,
        'w': 3,
        'affinity': "alchemy",
    },
    'lumber': { # tokenId 103
        'n': 5,
        'e': 1,
        's': 3,
        'w': 5,
        'affinity': "smithing",
    },
    'ox': { # tokenId 114
        'n': 5,
        'e': 5,
        's': 4,
        'w': 3,
        'affinity': "smithing",
    },
    'donkey': { # tokenId 76
        'n': 5,
        'e': 5,
        's': 5,
        'w': 5,
        'affinity': "leather working",
    },
    'common feather': { # tokenId 69
        'n': 6,
        'e': 1,
        's': 4,
        'w': 3,
        'affinity': "enchanting",
    },
    'grain': { # tokenId 93
        'n': 5,
        'e': 3,
        's': 3,
        'w': 4,
        'affinity': "brewing",
    },
    'common relic': { # tokenId 71
        'n': 6,
        'e': 2,
        's': 2,
        'w': 3,
        'affinity': "arcana",
    },
    'blue rupee': { # tokenId 49
        'n': 6,
        'e': 3,
        's': 1,
        'w': 3,
        'affinity': "enchanting",
    },
    # T5
    'half penny': { # tokenId 96
        'n': 4,
        'e': 2,
        's': 4,
        'w': 3,
        'affinity': "leather working",
    },
    'diamond': { # tokenId 73
        'n': 2,
        'e': 1,
        's': 6,
        'w': 1,
        'affinity': "alchemy",
    },
    'dragon tail': { # tokenId 77
        'n': 3,
        'e': 5,
        's': 2,
        'w': 1,
        'affinity': "brewing",
    },
    'gold coin': { # tokenId 92
        'n': 1,
        'e': 5,
        's': 4,
        'w': 1,
        'affinity': "smithing",
    },
    'beetle wings': { # tokenId 48
        'n': 2,
        'e': 1,
        's': 4,
        'w': 4,
        'affinity': "brewing",
    },
    'silver coin': { # tokenId 151
        'n': 2,
        'e': 3,
        's': 1,
        'w': 5,
        'affinity': "enchanting",
    },
    'pearl': { # tokenId 115
        'n': 6,
        'e': 1,
        's': 1,
        'w': 2,
        'affinity': "arcana",
    },
    'red rupee': { # tokenId 133
        'n': 1,
        'e': 3,
        's': 3,
        'w': 5,
        'affinity': "smithing",
    },
    'emerald': { # tokenId 79
        'n': 5,
        'e': 1,
        's': 1,
        'w': 3,
        'affinity': "alchemy",
    },
    'quarter penny': { # tokenId 117
        'n': 1,
        'e': 4,
        's': 1,
        'w': 5,
        'affinity': "leather working",
    },
    'none': {
        'n': ' ',
        'e': ' ',
        's': ' ',
        'w': ' ',
        'affinity': "none",
    },
}