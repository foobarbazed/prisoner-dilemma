from strategy import Strategy as Base

import random

class Strategy(Base):

    def __init__(self):
        self.name = "Eye For an Eye"
        self.description = "Repeats the opponent's previous move"

    def randomize(self, true_odds: int = 2, false_odds: int = 8):
        return random.choices((True, False), [true_odds, false_odds])[0]

    def play(self, moves: list[bool] = None, my_moves: list[bool] = None):
        if moves:
            if not moves[0]:
                return self.randomize()
            return self.randomize(9, 1)
        return True