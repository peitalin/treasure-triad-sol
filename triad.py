
import numpy as np
from params import CARDS
from render import render_grid



class TreasureTriad:

    def __init__(self):
        self.grid = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def __repr__(self):
        render_grid(self.grid)
        return ''


    def stake_treasure(self, treasure=None, coords=(0,0)):
        row = coords[0]
        col = coords[1]

        if self.grid[row][col] is None:
            self.grid[row][col] = treasure
            self.flip_adjacent_cells(coords=coords, player=treasure['player'])
        else:
            # throw error
            print('Slot occupied!')

        render_grid(self.grid)


    def flip_adjacent_cells(self, coords=(0,0), player='blue'):
        row = coords[0]
        col = coords[1]

        assert 0 <= row < 3
        assert 0 <= col < 3

        _current_card = self.grid[row][col]
        current_card = CARDS[_current_card['treasure']] if _current_card else None

        if current_card is None:
            return

        def card_above_treasure(row, col):
            if row-1 >= 0:
                above = self.grid[row-1][col]
                if above:
                    return CARDS[above['treasure']]

        def card_below_treasure(row, col):
            if row+1 <= 2:
                below = self.grid[row+1][col]
                if below:
                    return CARDS[below['treasure']]

        def card_left_of_treasure(row, col):
            if col-1 >= 0:
                left = self.grid[row][col-1]
                if left:
                    return CARDS[left['treasure']]

        def card_right_of_treasure(row, col):
            if col+1 <= 2:
                right = self.grid[row][col+1]
                if right:
                    return CARDS[right['treasure']]


        ## Check Card ABOVE
        card_above = card_above_treasure(row, col)
        if card_above:
            # compare top of current card to bottom of card above
            if current_card['n'] > card_above['s']:
                # if score on staked card is bigger, flip the card to new player
                self.grid[row-1][col]['player'] = player

        ## Check Card BELOW
        card_below = card_below_treasure(row, col)
        if card_below:
            # compare bottom of current card to top of card below
            if current_card['s'] > card_below['n']:
                self.grid[row+1][col]['player'] = player

        ## Check Card on the RIGHT
        card_on_the_right = card_right_of_treasure(row, col)
        if card_on_the_right:
            # compare east-side of current card to west-side of card on the right
            if current_card['e'] > card_on_the_right['w']:
                self.grid[row][col+1]['player'] = player

        ## Check Card on the LEFT
        card_on_the_left = card_left_of_treasure(row, col)
        if card_on_the_left:
            # compare west-side of current card to east-side of card on the left
            if current_card['w'] > card_on_the_left['e']:
                self.grid[row][col-1]['player'] = player




