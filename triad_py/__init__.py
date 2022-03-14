
from triad import TreasureTriad
import time
T = 0.75


size = 3
# size = 4
tt = TreasureTriad(size=size)
## Coords are zero-indexed

tt.stake_treasure({'treasure': 'dragon tail', 'player': 'nature'}, coords=(0,1))
time.sleep(T)

# flip left
tt.stake_treasure({'treasure': 'honeycomb', 'player': 'user'}, coords=(0,0))
time.sleep(T)

tt.stake_treasure({'treasure': 'grin', 'player': 'nature'}, coords=(1,0))
time.sleep(T)

# flip right
tt.stake_treasure({'treasure': 'ox', 'player': 'user'}, coords=(1,2))
time.sleep(T)

# flip below
tt.stake_treasure({'treasure': 'bottomless elixer', 'player': 'nature'}, coords=(0,2))
time.sleep(T)

# flip above
tt.stake_treasure({'treasure': 'donkey', 'player': 'user'}, coords=(1,1))
time.sleep(T)

tt.stake_treasure({'treasure': 'small bird', 'player': 'nature'}, coords=(2,2))
time.sleep(T)

tt.stake_treasure({'treasure': 'immovable stone', 'player': 'user'}, coords=(2,1))
time.sleep(T)

tt.stake_treasure({'treasure': 'red feather', 'player': 'nature'}, coords=(2,0))
time.sleep(T)

if size == 4:
    tt.stake_treasure({'treasure': 'castle', 'player': 'user'}, coords=(3,2))
    time.sleep(T)

    tt.stake_treasure({'treasure': 'ancient relic', 'player': 'nature'}, coords=(3,3))
    time.sleep(T)

    tt.stake_treasure({'treasure': 'military stipend', 'player': 'user'}, coords=(3,1))
    time.sleep(T)

    tt.stake_treasure({'treasure': 'cap of invisibility', 'player': 'nature'}, coords=(3,0))
    time.sleep(T)

    tt.stake_treasure({'treasure': 'pot of gold', 'player': 'user'}, coords=(1,3))
    time.sleep(T)

    tt.stake_treasure({'treasure': 'lumber', 'player': 'nature'}, coords=(2,3))
    time.sleep(T)

    tt.stake_treasure({'treasure': 'common bead', 'player': 'user'}, coords=(0,3))







### TODO
## Legions choose 1~5 treasures to use in the puzzle
## higher quest lvls => can take more treasures wit your (your deck)

## allow whitelisted foreign items as treasures (but with lower stats)
## Some cells in the grid have "corruption". Must win that cell or get trapped in stasis for 1 day

## Some cells have elements => specific
## if your legion has the right constellation, and class, you can buff your stats

