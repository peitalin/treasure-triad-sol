
import numpy as np
from params import CARDS, getAffinityBoost
from render import render_grid_3x3


# Player: "nature" | "user" | "none"
# StatusEffect:
#     "corruption"
#     | "alchemy"
#     | "arcana"
#     | "brewing"
#     | "enchanting"
#     | "leather"
#     | "smithing"

# • when treasure of same category is placed on the grid cell with the same category
# it gains a +1 boost, -1 otherwise
# • When a legion shares the same class as the slot, there is a +1 boost, 0 otherwise
# • A gridCell containing "corruption" must be controlled by the player otherwise their legion
# will enter a 1 day stasis lock

# Riverman: +1 Alchemy
# Numerariare: +1 Arcana
# Spellcaster: +1 Arcana, +1 Enchanting
# Assassin: +1 Brewing, +1 Leather
# Warrior: +1 Enchanting, +1 Smithing
# Ranger: +1 Leather, +1 Brewing
# Seige: +1 Smithing, +1 Alchemy
# All-class: +1 All Categories
# Common: None

affinitys = [
    "corruption",
    "alchemy",
    "arcana",
    "brewing",
    "enchanting",
    "leather",
    "smithing",
]
affinity_prob = [
    0.25,
    0.125,
    0.125,
    0.125,
    0.125,
    0.125,
    0.125,
]

grid_cells = [
    (0,0), (0,1), (0,2),
    (1,0), (1,1), (1,2),
    (2,0), (2,1), (2,2),
]




class TreasureTriad:

    def __init__(self, size=3):

        assert size == 3 or size == 4

        self.gridRows = size
        self.gridCols = size
        self.converted_cards = 0
        self.corrupted_cards = 0
        # corrupted cards on grid not under player's control

        # 3x3 grid
        # grid is zero-indexed
        grid = [
            [
                { "tcard": "", "player": "", 'affinity': ""},
                { "tcard": "", "player": "", 'affinity': ""},
                { "tcard": "", "player": "", 'affinity': ""}
            ],
            [
                { "tcard": "", "player": "", 'affinity': ""},
                { "tcard": "", "player": "", 'affinity': ""},
                { "tcard": "", "player": "", 'affinity': ""}
            ],
            [
                { "tcard": "", "player": "", 'affinity': ""},
                { "tcard": "", "player": "", 'affinity': ""},
                { "tcard": "", "player": "", 'affinity': ""}
            ],
        ]
        self.grid = grid;


    def init_grid(
        self,
        s_effects,
        effects_coords,
        natures_cards,
        natures_cards_coords,
        disable_status_effects=True,
        disable_natures_cards=True,
    ):
        # randomly select status effects and their positions
        # if not provided manually
        if not disable_status_effects:
            if not s_effects:
                s_effects = np.random.choice(
                    a=affinitys,    # choices
                    size=2,              # draw 2
                    p=affinity_prob # probabilities
                )
            if not effects_coords:
                effects_coords = np.random.choice(
                    a=[0,1,2,3,4,5,6,7,8],
                    size=2,
                    replace=False # No doubling up
                )


        # randomly select nature's cards and their positions
        # if not provided manually
        if not disable_natures_cards:
            if not natures_cards:
                natures_cards = np.random.choice(
                    a=list(CARDS.keys()),
                    size=3,
                )
            if not natures_cards_coords:
                natures_cards_coords = np.random.choice(
                    a=[0,1,2,3,4,5,6,7,8],
                    size=3,
                    replace=False # No doubling up
                )


        # apply effects and cards to grid
        for j, e_coords in enumerate(effects_coords):
            cellRef = grid_cells[e_coords] # (0,2)
            effect = s_effects[j]
            cell = self.grid[cellRef[0]][cellRef[1]]
            cell['affinity'] = effect
            # count number of corrupted cards needed to flip
            if effect == 'corruption':
                self.corrupted_cards += 1

        for i, n_coords in enumerate(natures_cards_coords):
            cellRef = grid_cells[n_coords] # (0,2)
            card_name = natures_cards[i]
            cell = self.grid[cellRef[0]][cellRef[1]]
            cell['tcard'] = card_name




    def __repr__(self):
        if self.gridRows == 3:
            render_grid_3x3(self.grid)
        elif self.gridRows == 4:
            render_grid_4x4(self.grid)
        # print("Converted Cards: ", self.converted_cards)
        return ''

    def increment_converted_cards(self, num_flips=0):
        self.converted_cards += num_flips

    def recalc_corrupted_cells(self):
        corrupt_cell_count = 0
        for row in self.grid:
            for cell in row:
                if cell['affinity'] == "corruption":
                    if cell['player'] == "" or cell['player'] == "nature":
                        corrupt_cell_count += 1

        self.corrupted_cards = corrupt_cell_count


    def stake_treasure(
        self,
        tcard={ "tcard": "", "player": ""},
        coords=(0,0)
    ):
        row = coords[0]
        col = coords[1]
        cell = self.grid[row][col]
        legion_class = tcard.get('player')

        if cell['tcard'] == "":
            # reassign tcard, player, and legion_class which placed the card for the cell
            # affinity is a property of the cell, never gets re-assigned
            cell['tcard'] = tcard['tcard']
            cell['player'] = tcard['player']

            if legion_class and legion_class != "nature":
                cell['player'] = legion_class

            self.try_flip_adjacent_cards(
                coords=coords,
                player=tcard['player'],
            )
        else:
            # throw error
            print('Slot occupied!')

        render_grid_3x3(self.grid, legion_class)
        print("Converted Cards: ", self.converted_cards)
        print("#Corrupted Cells: ", self.corrupted_cards)



    def try_flip_adjacent_cards(self, coords=(0,0), player='common'):

        row = coords[0]
        col = coords[1]

        assert 0 <= row < self.gridRows
        assert 0 <= col < self.gridCols

        current_cell = self.grid[row][col]
        current_card = CARDS[current_cell['tcard']] if current_cell['tcard'] else None
        legion_class = player

        if current_card is None:
            return

        def getCardAboveTreasure(row, col):
            # check card above is in the grid
            if row-1 >= 0:
                above = self.grid[row-1][col]
                if above['tcard']:
                    return CARDS[above['tcard']]

        def getCardBelowTreasure(row, col):
            # check card below is in the grid
            if row+1 <= self.gridRows-1:
                below = self.grid[row+1][col]
                if below['tcard']:
                    return CARDS[below['tcard']]

        def getCardLeftOfTreasure(row, col):
            # check card to left is in the grid
            if col-1 >= 0:
                left = self.grid[row][col-1]
                if left['tcard']:
                    return CARDS[left['tcard']]

        def getCardRightOfTreasure(row, col):
            # check card to right is in the grid
            if col+1 <= self.gridCols-1:
                right = self.grid[row][col+1]
                if right['tcard']:
                    return CARDS[right['tcard']]



        # • when treasure of same category is placed on the grid cell with the same category
        # it gains a +1 boost, -1 otherwise
        # • When a legion shares the same class as the slot, there is a +1 boost, 0 otherwise
        # • A gridCell containing "corruption" must be converted by the player otherwise their legion
        # will enter a 1 day stasis lock

        card_flips = 0
        affinity_boost = getAffinityBoost(
            current_cell['affinity'],
            current_card['affinity'],
            legion_class
        )


        ## Try flip Card ABOVE
        card_above = getCardAboveTreasure(row, col)
        if card_above:
            # compare north of current card to south of card above
            if current_card['n'] + affinity_boost > card_above['s']:
                # if score on staked card is bigger, flip the card to new player
                self.grid[row-1][col]['player'] = player
                if player == "nature":
                    card_flips -= 1
                else:
                    card_flips += 1


        ## Try flip Card BELOW
        card_below = getCardBelowTreasure(row, col)
        if card_below:
            # compare south of current card to north of card below
            if current_card['s'] + affinity_boost > card_below['n']:
                self.grid[row+1][col]['player'] = player
                if player == "nature":
                    card_flips -= 1
                else:
                    card_flips += 1


        ## Try flip Card on the LEFT
        card_on_the_left = getCardLeftOfTreasure(row, col)
        if card_on_the_left:
            # compare west-side of current card to east-side of card on the left
            if current_card['w'] + affinity_boost > card_on_the_left['e']:
                self.grid[row][col-1]['player'] = player
                if player == "nature":
                    card_flips -= 1
                else:
                    card_flips += 1


        ## Try flip Card on the RIGHT
        card_on_the_right = getCardRightOfTreasure(row, col)
        if card_on_the_right:
            # compare east-side of current card to west-side of card on the right
            if current_card['e'] + affinity_boost > card_on_the_right['w']:
                self.grid[row][col+1]['player'] = player
                if player == "nature":
                    card_flips -= 1
                else:
                    card_flips += 1

        self.recalc_corrupted_cells()
        self.increment_converted_cards(card_flips)


