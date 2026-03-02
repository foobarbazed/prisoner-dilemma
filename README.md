# prisoner's dilemma python thing

you need python installed to run it of course

to play with defaults:
```
python main.py
```
if you want to see what options you have, just use --help:
```
python main.py --help
```
example:
```
python main.py --games 10 --turns 200 --noise 0
```

example output:
```
RESULTS
10 games of 200 turns for every strat combination, max points being 70000, with a noise chance of 0% and no knowledge about being misunderstood

    [██████████████████████████████████                ]    Statistic: score of 69.18 (48426/70000 points) - Chooses the most common move after 10 moves
    [██████████████████████████████████                ]    Eye For an Eye: score of 69.17 (48422/70000 points) - Repeats the opponent's previous move
    [██████████████████████████████████                ]    Zombie: score of 69.15 (48406/70000 points) - Chooses the least common move after 10 moves
    [██████████████████████████████████                ]    Petty: score of 69.14 (48400/70000 points) - Holds grudges against you, does not forgive easily
    [██████████████████████████████████                ]    Aggressive: score of 69.14 (48400/70000 points) - Smart, but tends to betray
    [██████████████████████████████████                ]    Smart: score of 69.11 (48376/70000 points) - Generous Eye for an Eye, understands misunderstandings, forgives
    [███████████████████████████████                   ]    Sneaky: score of 62.75 (43925/70000 points) - Eye for an Eye, but can sabotage

WINNER: Statistic
```