
from triad import TreasureTriad
import time
T = 0.75



## Legions choose 1~5 treasures to use in the puzzle
## higher constellation lvls => can take more treasures wit your (your deck)
## allow whitelisted foreign items as treasures (but with lower stats)

size = 3
tt = TreasureTriad(size=size)
# no status effects, no cards placed for nature/computer
tt.init_grid(
    s_effects=[],
    effects_coords=[],
    natures_cards=[],
    natures_cards_coords=[],
    disable_status_effects=True,
    disable_natures_cards=True,
)
tt.grid

# flip left
tt.stake_treasure({'tcard': 'dragon tail', 'player': 'nature' }, coords=(0,1))
time.sleep(T)

tt.stake_treasure({'tcard': 'honeycomb', 'player': 'user'}, coords=(0,0))
time.sleep(T)

tt.stake_treasure({'tcard': 'grin', 'player': 'nature'}, coords=(1,0))
time.sleep(T)

# flip right
tt.stake_treasure({'tcard': 'ox', 'player': 'user' }, coords=(1,2))
time.sleep(T)

# flip below
tt.stake_treasure({'tcard': 'bottomless elixer', 'player': 'nature'}, coords=(0,2))
time.sleep(T)

# flip above
tt.stake_treasure({'tcard': 'donkey', 'player': 'user' }, coords=(1,1))
time.sleep(T)

tt.stake_treasure({'tcard': 'small bird', 'player': 'nature'}, coords=(2,2))
time.sleep(T)

tt.stake_treasure({'tcard': 'immovable stone', 'player': 'user' }, coords=(2,1))
time.sleep(T)

tt.stake_treasure({'tcard': 'red feather', 'player': 'nature'}, coords=(2,0))
time.sleep(T)




############### Scenario 2 ##############
#### Testing +2 affinity boost flips cards on N, E, S, W directions

size = 3
tt = TreasureTriad(size=size)
# place "leather working" status effect on 5th cell (1,1)
tt.init_grid(
    s_effects=["leather working"],
    effects_coords=[4], # 5th cell [4] is (1,1)
    natures_cards=[],
    natures_cards_coords=[],
    disable_status_effects=False,
    disable_natures_cards=True,
)
legion_class = 'assassin'
## assassin affinity = leather working + brewing

# South: 6
tt.stake_treasure(
    {'tcard': 'bait for monsters', 'player': 'nature', 'legion_class': ''},
    coords=(0,1)
)
time.sleep(T)

# East: 6
tt.stake_treasure(
    {'tcard': 'mollusk shell', 'player': 'nature', 'legion_class': ''},
    coords=(1,0)
)
time.sleep(T)

# West: 6
tt.stake_treasure(
    {'tcard': 'common bead', 'player': 'nature', 'legion_class': ''},
    coords=(1,2)
)
time.sleep(T)

# North: 6
tt.stake_treasure(
    {'tcard': 'jar of fairies', 'player': 'nature', 'legion_class': ''},
    coords=(2,1)
)
time.sleep(T)

# Donkey has 5 stats all around, boosted to 7 all around
tt.stake_treasure(
    {'tcard': 'donkey', 'player': 'user', 'legion_class': legion_class},
    coords=(1,1)
)
print("\nDonkey has +5 stats all around, boosted to +7 and converted 4 surrounding cards because:")
print("\tlegion placing the card has leather working affinity: ", legion_class)
print("\tdonkey card has leather working affinity")




# if size == 4:
#     tt.stake_treasure({'tcard': 'castle', 'player': 'user'}, coords=(3,2))
#     time.sleep(T)

#     tt.stake_treasure({'tcard': 'ancient relic', 'player': 'nature'}, coords=(3,3))
#     time.sleep(T)

#     tt.stake_treasure({'tcard': 'military stipend', 'player': 'user'}, coords=(3,1))
#     time.sleep(T)

#     tt.stake_treasure({'tcard': 'cap of invisibility', 'player': 'nature'}, coords=(3,0))
#     time.sleep(T)

#     tt.stake_treasure({'tcard': 'pot of gold', 'player': 'user'}, coords=(1,3))
#     time.sleep(T)

#     tt.stake_treasure({'tcard': 'lumber', 'player': 'nature'}, coords=(2,3))
#     time.sleep(T)

#     tt.stake_treasure({'tcard': 'common bead', 'player': 'user'}, coords=(0,3))




