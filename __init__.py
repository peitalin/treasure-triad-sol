
from triad import TreasureTriad


tt = TreasureTriad()
## Coords are zero-indexed

tt.stake_treasure({'treasure': 'dragon tail', 'player': 'red'}, coords=(0,1))
# flip left
tt.stake_treasure({'treasure': 'honeycomb', 'player': 'blue'}, coords=(0,0))
# flip right
tt.stake_treasure({'treasure': 'ox', 'player': 'blue'}, coords=(1,2))
# flip below
tt.stake_treasure({'treasure': 'bottomless elixer', 'player': 'red'}, coords=(0,2))
# flip above
tt.stake_treasure({'treasure': 'donkey', 'player': 'blue'}, coords=(1,1))


### TODO
## Legions are a card as well

## Legions choose 1~5 treasures to use in the puzzle
## higher quest lvls => more treasures to take

## allow whitelistsed foreign items as treasures (but with lower stats)