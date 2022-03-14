
import numpy as np
from params import CARDS
from render import render_grid_3x3, render_grid_4x4



class TreasureTriad:

    def __init__(self, size=3):
        assert size == 3 or size == 4
        self.gridRows = size
        self.gridCols = size
        if size == 3:
            self.grid = [
                [{ "treasure": None, "player": None}, { "treasure": None, "player": None}, { "treasure": None, "player": None}],
                [{ "treasure": None, "player": None}, { "treasure": None, "player": None}, { "treasure": None, "player": None}],
                [{ "treasure": None, "player": None}, { "treasure": None, "player": None}, { "treasure": None, "player": None}],
            ]
        elif size ==4:
            self.grid = [
                [{ "treasure": None, "player": None}, { "treasure": None, "player": None}, { "treasure": None, "player": None}, { "treasure": None, "player": None}],
                [{ "treasure": None, "player": None}, { "treasure": None, "player": None}, { "treasure": None, "player": None}, { "treasure": None, "player": None}],
                [{ "treasure": None, "player": None}, { "treasure": None, "player": None}, { "treasure": None, "player": None}, { "treasure": None, "player": None}],
                [{ "treasure": None, "player": None}, { "treasure": None, "player": None}, { "treasure": None, "player": None}, { "treasure": None, "player": None}],
            ]
        # 3x3 or 4x4 grid
        # grid is zero-indexed
        self.converted_cards = 0

    def __repr__(self):
        if self.rows == 3:
            render_grid_3x3(self.grid)
        elif self.rows == 4:
            render_grid_4x4(self.grid)
        # print("Converted Cards: ", self.converted_cards)
        return ''

    def count_converted_cards(self):
        converted_cards = 0
        for row in self.grid:
            for cell in row:
                if cell['player'] == 'user':
                    converted_cards += 1
        self.converted_cards = converted_cards


    def stake_treasure(self, treasure={ "treasure": None, "player": None}, coords=(0,0)):
        row = coords[0]
        col = coords[1]

        if self.grid[row][col]['treasure'] is None:
            self.grid[row][col] = treasure
            self.try_flip_adjacent_cards(coords=coords, player=treasure['player'])
        else:
            # throw error
            print('Slot occupied!')

        if self.gridRows == 3:
            render_grid_3x3(self.grid)
        elif self.gridRows == 4:
            render_grid_4x4(self.grid)



    def try_flip_adjacent_cards(self, coords=(0,0), player='user'):
        row = coords[0]
        col = coords[1]

        assert 0 <= row < self.gridRows
        assert 0 <= col < self.gridCols

        _current_card = self.grid[row][col]
        current_card = CARDS[_current_card['treasure']] if _current_card['treasure'] else None
        print('current', current_card)

        if current_card is None:
            return

        def getCardAboveTreasure(row, col):
            # check card above is in the grid
            if row-1 >= 0:
                above = self.grid[row-1][col]
                if above['treasure']:
                    return CARDS[above['treasure']]

        def getCardBelowTreasure(row, col):
            # check card below is in the grid
            if row+1 < self.gridRows-1:
                below = self.grid[row+1][col]
                if below['treasure']:
                    return CARDS[below['treasure']]

        def getCardLeftOfTreasure(row, col):
            # check card to left is in the grid
            if col-1 >= 0:
                left = self.grid[row][col-1]
                if left['treasure']:
                    return CARDS[left['treasure']]

        def getCardRightOfTreasure(row, col):
            # check card to right is in the grid
            if col+1 < self.gridCols-1:
                right = self.grid[row][col+1]
                if right['treasure']:
                    return CARDS[right['treasure']]


        ## Try flip Card ABOVE
        card_above = getCardAboveTreasure(row, col)
        if card_above:
            # compare top of current card to bottom of card above
            if current_card['n'] > card_above['s']:
                # if score on staked card is bigger, flip the card to new player
                self.grid[row-1][col]['player'] = player

        ## Try flip Card BELOW
        card_below = getCardBelowTreasure(row, col)
        if card_below:
            # compare bottom of current card to top of card below
            if current_card['s'] > card_below['n']:
                self.grid[row+1][col]['player'] = player

        ## Try flip Card on the LEFT
        card_on_the_left = getCardLeftOfTreasure(row, col)
        if card_on_the_left:
            # compare west-side of current card to east-side of card on the left
            if current_card['w'] > card_on_the_left['e']:
                self.grid[row][col-1]['player'] = player

        ## Try flip Card on the RIGHT
        card_on_the_right = getCardRightOfTreasure(row, col)
        if card_on_the_right:
            # compare east-side of current card to west-side of card on the right
            if current_card['e'] > card_on_the_right['w']:
                self.grid[row][col+1]['player'] = player




