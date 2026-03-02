import argparse

from game import Game

# defaults
GAMES = 50
TURNS = 100
NOISE = 10 # %
STRATEGIES_UNDERSTAND_NOISE = False
EXCLUDE_STRATEGIES = ["alwaystrue", "alwaysfalse", "random", "tester"]
VERBOSE = False

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-g", "--games", type=int, help="How many games each strat plays with each other strat", default=GAMES)
parser.add_argument("-t", "--turns", type=int, help="Each gmae has this amount of turns", default=TURNS)
parser.add_argument("-n", "--noise", type=int, help="Percentage between 0 and 100", default=NOISE)
parser.add_argument("-N", "--strategies-understand-noise", action="store_true", help="Whether strats understand they've been misunderstood (noise) or no", default=STRATEGIES_UNDERSTAND_NOISE)
parser.add_argument("-e", "--exclude-strategies", type=list, help="List of strategies to exclude from the game", default=EXCLUDE_STRATEGIES)
parser.add_argument("-v", "--verbose", action="store_true")

args = parser.parse_args()
GAMES = args.games
TURNS = args.turns
NOISE = args.noise
STRATEGIES_UNDERSTAND_NOISE = args.strategies_understand_noise
EXCLUDE_STRATEGIES = args.exclude_strategies
VERBOSE = args.verbose

def bar(progress: int, total: int, length: int = 50):
    percent = 100*(progress/total)
    filled = int(length * progress // total)
    string = '█'*filled+' '*(length-filled)
    return string

if __name__ == "__main__":

    game = Game(
        games = GAMES,
        turns = TURNS,
        noise = NOISE,
        understanding = STRATEGIES_UNDERSTAND_NOISE,
        exclude = EXCLUDE_STRATEGIES,
        verbose = VERBOSE
        )

    game.play()

    maximum = GAMES*TURNS*5*len(game.strategies)

    winner = "None"
    winner_amount = 0

    results = {}

    for strat, result in game.results.items():
        results[strat] = sum(result)

    results = {key: results[key] for key in sorted(results, key=results.get, reverse = True)}

    print("\n\nRESULTS")
    print(f"{GAMES} games of {TURNS} turns for every strat combination, \
max points being {maximum}, with a noise chance of {NOISE}% {f'(1/{(round(100/NOISE))}) ' if NOISE > 0 else ''}\
and {'no ' if not STRATEGIES_UNDERSTAND_NOISE else ''}knowledge about being misunderstood\n")

    for strat, result in results.items():
        if winner_amount < result:
            winner_amount = result
            winner = strat

        description = game.descriptions[strat]
        percent = result/maximum*100

        print(f"    [{bar(result, maximum)}]    {strat}: score of {round(percent, 2)} ({result}/{maximum} points) - {description}")


    print(f"\nWINNER: {winner}")



