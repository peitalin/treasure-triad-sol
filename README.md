
## Treasure Triad

Treasure staking puzzle game
- 3x3 Grid with randomly placed cards
- each card has 4 sides with scores on them
- place cards on the grid to flip existing cards to your color
- if a card's score on a side is bigger than another card's score it flips to your color


### Game Variations
- Either we have 2 stages of the game: "Nature" places 3 cards initially, then "user" tries to convert as maybe cards as they can
- Or "Nature" and "user" take turns placing 1 card down each


### Python demo
install libraries
```
pip3 install numpy
pip3 install termcolor
```
run Treasure Triad demo
```
python3 ./triad_py/__init__.py
```


### Solidity demo

`npx hardhat test` runs the same steps as the python script and checks that cards are flipped each step

```
cd triad_sol
yarn install
npx hardhat compile
npx hardhat test
```