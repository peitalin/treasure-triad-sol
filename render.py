import numpy as np
import os
from termcolor import colored, cprint
from params import CARDS


## for drawing grid only
## Ignore for solidity implementation


def fmt_treasure(s, max_len=15):
    "Truncates/pads a treasure's name to fit a fixed length grid"
    if len(s) >= max_len:
        new_s = s[:max_len]
    else:
        i = 0
        new_s = s
        while len(new_s) < max_len:
            if i % 2 == 0:
                new_s = new_s + " "
            else:
                new_s = " " + new_s
            i += 1

    return new_s


def red(s):
    return colored(s, 'red')

def blue(s):
    return colored(s, 'blue')


def render_card(card={ 'treasure': 'grin', 'player': 'blue'}):
    if card is None:
        return {
            'treasure': fmt_treasure(''),
            'n': ' ',
            'e': ' ',
            's': ' ',
            'w': ' ',
        }

    t = card['treasure']
    return {
        'treasure': fmt_treasure(t),
        'n': blue(CARDS[t]['n']),
        'e': blue(CARDS[t]['e']),
        's': blue(CARDS[t]['s']),
        'w': blue(CARDS[t]['w']),
    } if card['player'] == 'blue' else {
        'treasure': fmt_treasure(t),
        'n': red(CARDS[t]['n']),
        'e': red(CARDS[t]['e']),
        's': red(CARDS[t]['s']),
        'w': red(CARDS[t]['w']),
    }


def render_grid_3x3(grid=[
    [ None, None, None ],
    [ None, None, None ],
    [ None, None, None ],
]):

    c0_0 = render_card(grid[0][0])
    c0_1 = render_card(grid[0][1])
    c0_2 = render_card(grid[0][2])
    c1_0 = render_card(grid[1][0])
    c1_1 = render_card(grid[1][1])
    c1_2 = render_card(grid[1][2])
    c2_0 = render_card(grid[2][0])
    c2_1 = render_card(grid[2][1])
    c2_2 = render_card(grid[2][2])

    a = """
    -------------------------------------------------------------
    |         {c0_0_n}         |         {c0_1_n}         |         {c0_2_n}         |
    |                   |                   |                   |
    |                   |                   |                   |
    |{c0_0_w} {c0_0_treasure} {c0_0_e}|{c0_1_w} {c0_1_treasure} {c0_1_e}|{c0_2_w} {c0_2_treasure} {c0_2_e}|
    |                   |                   |                   |
    |                   |                   |                   |
    |         {c0_0_s}         |         {c0_1_s}         |         {c0_2_s}         |
    -------------------------------------------------------------
    |         {c1_0_n}         |         {c1_1_n}         |         {c1_2_n}         |
    |                   |                   |                   |
    |                   |                   |                   |
    |{c1_0_w} {c1_0_treasure} {c1_0_e}|{c1_1_w} {c1_1_treasure} {c1_1_e}|{c1_2_w} {c1_2_treasure} {c1_2_e}|
    |                   |                   |                   |
    |                   |                   |                   |
    |         {c1_0_s}         |         {c1_1_s}         |         {c1_2_s}         |
    -------------------------------------------------------------
    |         {c2_0_n}         |         {c2_1_n}         |         {c2_2_n}         |
    |                   |                   |                   |
    |                   |                   |                   |
    |{c2_0_w} {c2_0_treasure} {c2_0_e}|{c2_1_w} {c2_1_treasure} {c2_1_e}|{c2_2_w} {c2_2_treasure} {c2_2_e}|
    |                   |                   |                   |
    |                   |                   |                   |
    |         {c2_0_s}         |         {c2_1_s}         |         {c2_2_s}         |
    -------------------------------------------------------------
    """.format(
        # cell (0, 0)
        c0_0_treasure=fmt_treasure(c0_0['treasure']),
        c0_0_n=c0_0['n'],
        c0_0_e=c0_0['e'],
        c0_0_s=c0_0['s'],
        c0_0_w=c0_0['w'],
        # cell (0, 1)
        c0_1_treasure=fmt_treasure(c0_1['treasure']),
        c0_1_n=c0_1['n'],
        c0_1_e=c0_1['e'],
        c0_1_s=c0_1['s'],
        c0_1_w=c0_1['w'],
        # cell (0, 2)
        c0_2_treasure=fmt_treasure(c0_2['treasure']),
        c0_2_n=c0_2['n'],
        c0_2_e=c0_2['e'],
        c0_2_s=c0_2['s'],
        c0_2_w=c0_2['w'],
        # cell (1, 0)
        c1_0_treasure=fmt_treasure(c1_0['treasure']),
        c1_0_n=c1_0['n'],
        c1_0_e=c1_0['e'],
        c1_0_s=c1_0['s'],
        c1_0_w=c1_0['w'],
        # cell (1, 1)
        c1_1_treasure=fmt_treasure(c1_1['treasure']),
        c1_1_n=c1_1['n'],
        c1_1_e=c1_1['e'],
        c1_1_s=c1_1['s'],
        c1_1_w=c1_1['w'],
        # cell (1, 2)
        c1_2_treasure=fmt_treasure(c1_2['treasure']),
        c1_2_n=c1_2['n'],
        c1_2_e=c1_2['e'],
        c1_2_s=c1_2['s'],
        c1_2_w=c1_2['w'],
        # cell (2, 0)
        c2_0_treasure=fmt_treasure(c2_0['treasure']),
        c2_0_n=c2_0['n'],
        c2_0_e=c2_0['e'],
        c2_0_s=c2_0['s'],
        c2_0_w=c2_0['w'],
        # cell (2, 1)
        c2_1_treasure=fmt_treasure(c2_1['treasure']),
        c2_1_n=c2_1['n'],
        c2_1_e=c2_1['e'],
        c2_1_s=c2_1['s'],
        c2_1_w=c2_1['w'],
        # cell (2, 2)
        c2_2_treasure=fmt_treasure(c2_2['treasure']),
        c2_2_n=c2_2['n'],
        c2_2_e=c2_2['e'],
        c2_2_s=c2_2['s'],
        c2_2_w=c2_2['w'],
    )
    # return a
    os.system('clear')
    print(a)
    return a



def render_grid_4x4(grid=[
    [ None, None, None, None ],
    [ None, None, None, None ],
    [ None, None, None, None ],
]):

    c0_0 = render_card(grid[0][0])
    c0_1 = render_card(grid[0][1])
    c0_2 = render_card(grid[0][2])
    c0_3 = render_card(grid[0][3])

    c1_0 = render_card(grid[1][0])
    c1_1 = render_card(grid[1][1])
    c1_2 = render_card(grid[1][2])
    c1_3 = render_card(grid[1][3])

    c2_0 = render_card(grid[2][0])
    c2_1 = render_card(grid[2][1])
    c2_2 = render_card(grid[2][2])
    c2_3 = render_card(grid[2][3])

    c3_0 = render_card(grid[3][0])
    c3_1 = render_card(grid[3][1])
    c3_2 = render_card(grid[3][2])
    c3_3 = render_card(grid[3][3])

    a = """
    --------------------------------------------------------------------------------
    |         {c0_0_n}         |         {c0_1_n}         |         {c0_2_n}         |         {c0_3_n}         |
    |                   |                   |                   |                   |
    |                   |                   |                   |                   |
    |{c0_0_w} {c0_0_treasure} {c0_0_e}|{c0_1_w} {c0_1_treasure} {c0_1_e}|{c0_2_w} {c0_2_treasure} {c0_2_e}|{c0_3_w} {c0_3_treasure} {c0_3_e}|
    |                   |                   |                   |                   |
    |                   |                   |                   |                   |
    |         {c0_0_s}         |         {c0_1_s}         |         {c0_2_s}         |         {c0_3_s}         |
    --------------------------------------------------------------------------------
    |         {c1_0_n}         |         {c1_1_n}         |         {c1_2_n}         |         {c1_3_n}         |
    |                   |                   |                   |                   |
    |                   |                   |                   |                   |
    |{c1_0_w} {c1_0_treasure} {c1_0_e}|{c1_1_w} {c1_1_treasure} {c1_1_e}|{c1_2_w} {c1_2_treasure} {c1_2_e}|{c1_3_w} {c1_3_treasure} {c1_3_e}|
    |                   |                   |                   |                   |
    |                   |                   |                   |                   |
    |         {c1_0_s}         |         {c1_1_s}         |         {c1_2_s}         |         {c1_3_s}         |
    --------------------------------------------------------------------------------
    |         {c2_0_n}         |         {c2_1_n}         |         {c2_2_n}         |         {c2_3_n}         |
    |                   |                   |                   |                   |
    |                   |                   |                   |                   |
    |{c2_0_w} {c2_0_treasure} {c2_0_e}|{c2_1_w} {c2_1_treasure} {c2_1_e}|{c2_2_w} {c2_2_treasure} {c2_2_e}|{c2_3_w} {c2_3_treasure} {c2_3_e}|
    |                   |                   |                   |                   |
    |                   |                   |                   |                   |
    |         {c2_0_s}         |         {c2_1_s}         |         {c2_2_s}         |         {c2_3_s}         |
    --------------------------------------------------------------------------------
    |         {c3_0_n}         |         {c3_1_n}         |         {c3_2_n}         |         {c3_3_n}         |
    |                   |                   |                   |                   |
    |                   |                   |                   |                   |
    |{c3_0_w} {c3_0_treasure} {c3_0_e}|{c3_1_w} {c3_1_treasure} {c3_1_e}|{c3_2_w} {c3_2_treasure} {c3_2_e}|{c3_3_w} {c3_3_treasure} {c3_3_e}|
    |                   |                   |                   |                   |
    |                   |                   |                   |                   |
    |         {c3_0_s}         |         {c3_1_s}         |         {c3_2_s}         |         {c3_3_s}         |
    --------------------------------------------------------------------------------
    """.format(
        # cell (0, 0)
        c0_0_treasure=fmt_treasure(c0_0['treasure']),
        c0_0_n=c0_0['n'],
        c0_0_e=c0_0['e'],
        c0_0_s=c0_0['s'],
        c0_0_w=c0_0['w'],
        # cell (0, 1)
        c0_1_treasure=fmt_treasure(c0_1['treasure']),
        c0_1_n=c0_1['n'],
        c0_1_e=c0_1['e'],
        c0_1_s=c0_1['s'],
        c0_1_w=c0_1['w'],
        # cell (0, 2)
        c0_2_treasure=fmt_treasure(c0_2['treasure']),
        c0_2_n=c0_2['n'],
        c0_2_e=c0_2['e'],
        c0_2_s=c0_2['s'],
        c0_2_w=c0_2['w'],
        # cell (0, 3)
        c0_3_treasure=fmt_treasure(c0_3['treasure']),
        c0_3_n=c0_3['n'],
        c0_3_e=c0_3['e'],
        c0_3_s=c0_3['s'],
        c0_3_w=c0_3['w'],
        # cell (1, 0)
        c1_0_treasure=fmt_treasure(c1_0['treasure']),
        c1_0_n=c1_0['n'],
        c1_0_e=c1_0['e'],
        c1_0_s=c1_0['s'],
        c1_0_w=c1_0['w'],
        # cell (1, 1)
        c1_1_treasure=fmt_treasure(c1_1['treasure']),
        c1_1_n=c1_1['n'],
        c1_1_e=c1_1['e'],
        c1_1_s=c1_1['s'],
        c1_1_w=c1_1['w'],
        # cell (1, 2)
        c1_2_treasure=fmt_treasure(c1_2['treasure']),
        c1_2_n=c1_2['n'],
        c1_2_e=c1_2['e'],
        c1_2_s=c1_2['s'],
        c1_2_w=c1_2['w'],
        # cell (1, 3)
        c1_3_treasure=fmt_treasure(c1_3['treasure']),
        c1_3_n=c1_3['n'],
        c1_3_e=c1_3['e'],
        c1_3_s=c1_3['s'],
        c1_3_w=c1_3['w'],
        # cell (2, 0)
        c2_0_treasure=fmt_treasure(c2_0['treasure']),
        c2_0_n=c2_0['n'],
        c2_0_e=c2_0['e'],
        c2_0_s=c2_0['s'],
        c2_0_w=c2_0['w'],
        # cell (2, 1)
        c2_1_treasure=fmt_treasure(c2_1['treasure']),
        c2_1_n=c2_1['n'],
        c2_1_e=c2_1['e'],
        c2_1_s=c2_1['s'],
        c2_1_w=c2_1['w'],
        # cell (2, 2)
        c2_2_treasure=fmt_treasure(c2_2['treasure']),
        c2_2_n=c2_2['n'],
        c2_2_e=c2_2['e'],
        c2_2_s=c2_2['s'],
        c2_2_w=c2_2['w'],
        # cell (2, 3)
        c2_3_treasure=fmt_treasure(c2_3['treasure']),
        c2_3_n=c2_3['n'],
        c2_3_e=c2_3['e'],
        c2_3_s=c2_3['s'],
        c2_3_w=c2_3['w'],
        # cell (3, 0)
        c3_0_treasure=fmt_treasure(c3_0['treasure']),
        c3_0_n=c3_0['n'],
        c3_0_e=c3_0['e'],
        c3_0_s=c3_0['s'],
        c3_0_w=c3_0['w'],
        # cell (3, 1)
        c3_1_treasure=fmt_treasure(c3_1['treasure']),
        c3_1_n=c3_1['n'],
        c3_1_e=c3_1['e'],
        c3_1_s=c3_1['s'],
        c3_1_w=c3_1['w'],
        # cell (3, 2)
        c3_2_treasure=fmt_treasure(c3_2['treasure']),
        c3_2_n=c3_2['n'],
        c3_2_e=c3_2['e'],
        c3_2_s=c3_2['s'],
        c3_2_w=c3_2['w'],
        # cell (3, 3)
        c3_3_treasure=fmt_treasure(c3_3['treasure']),
        c3_3_n=c3_3['n'],
        c3_3_e=c3_3['e'],
        c3_3_s=c3_3['s'],
        c3_3_w=c3_3['w'],
    )
    # return a
    os.system('clear')
    print(a)
    return a