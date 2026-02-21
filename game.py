import os
import importlib
import multiprocessing
import random

from strategy import Strategy

class Game:

    def __init__(self, games: int = 1, turns: int = 100, noise: int = 0, understanding: bool = True, exclude: list[str] = list(), verbose: bool = False):

        self.strategies = []
        self.descriptions = {}
        self.pairs = []
        self.results = {}

        self.exclude = exclude
        self.turns = turns
        self.games = games
        self.noise = noise
        self.understanding = understanding
        self.verbose = verbose

        self.load_strategies()
        self.load_descriptions()
        self.generate_pairs()

        self.chunk_size = max(1, len(self.pairs) // 8 * (multiprocessing.cpu_count()))

        self.conditions = {
            (False, False): (1, 1),
            (True, True): (3, 3),
            (True, False): (5, 0),
            (False, True): (0, 5),
        }

    def print(self, string: str):
        if self.verbose: print(string)

    def load_strategies(self):
        fp = os.path.dirname(__file__)+"/strategies"

        for strat_path in os.listdir(fp):
            if strat_path.endswith(".py"):
                if strat_path[:-3] not in self.exclude:
                    module = importlib.import_module("strategies."+strat_path[:-3])
                    self.strategies.append(module.Strategy)

    def load_descriptions(self):
        for strategy in self.strategies:
            strategy = strategy()
            self.descriptions[strategy.name] = strategy.description

    def generate_pairs(self):

        amt = len(self.strategies)
        self.pairs = list((i, j) for i in range(amt) for j in range(i, amt))


    def simulate_game(self, p1: Strategy, p2: Strategy, amount: int) -> dict[str: int, str: int]:

        true_moves1 = list()
        moves1 = list()
        gain1 = int
        true_moves2 = list()
        gain2 = int
        moves2 = list()
        points = dict()

        for _ in range(amount):

            my_moves1 = moves1
            if self.understanding:
                my_moves1 = true_moves1
            result1 = p1.play(moves=true_moves2.copy().reverse(), my_moves=my_moves1.copy().reverse())
            true_moves1.append(result1)
            if self.noise != 0 and random.choices((True, False), [1, 100-self.noise])[0]:
                result1 = not result1
            moves1.append(result1)

            my_moves2 = moves2
            if self.understanding:
                my_moves2 = true_moves2
            result2 = p2.play(moves=true_moves1.copy().reverse(), my_moves=my_moves2.copy().reverse())
            true_moves2.append(result2)
            if self.noise != 0 and random.choices((True, False), [1, 100-self.noise])[0]:
                result2 = not result2
            moves2.append(result2)

            gain1, gain2 = self.conditions[(result1, result2)]

            points[p1.name] = points.get(p1.name, 0) + gain1
            points[p2.name] = points.get(p2.name, 0) + gain2

        return points
    
    def worker(self, pair: tuple[int, int]) -> dict[str: int, str: int]:
        i1, i2 = pair
        p1, p2 = self.strategies[i1], self.strategies[i2]
        final_results = {}
        for game in range(self.games):
            result = self.simulate_game(p1(), p2(), self.turns)
            for strat, points in result.items():
                if not strat in final_results:
                    final_results[strat] = []
                final_results[strat].append(points)
        p1, p2 = p1(), p2()
        sum1 = sum(final_results[p1.name])
        sum2 = sum(final_results[p2.name])
        self.print(f"{p1.name} + {p2.name} | {p1.name} - points gain: {sum1} (avg {round(sum1/self.turns, 2)}) | {p2.name} - points gain: {sum2} (avg {round(sum2/self.turns, 2)})")
        return final_results


    def play(self):

        with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
            results = pool.imap(self.worker, self.pairs, chunksize=self.chunk_size)

            for result in results:
                for strat, points in result.items():
                    if not strat in self.results:
                        self.results[strat] = []
                    for point in points:
                        self.results[strat].append(point)
