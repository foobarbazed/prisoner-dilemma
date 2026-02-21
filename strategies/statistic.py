from strategy import Strategy as Base

import random

class Strategy(Base):

    def __init__(self):
        self.name = "Statistic"
        self.description = "Chooses the most common move after 10 moves"

    def randomize(self, true_odds: int = 2, false_odds: int = 8):
        return random.choices((True, False), [true_odds, false_odds])[0]

    def play(self, moves: list[bool] = None, my_moves: list[bool] = None):
        if moves:
            if len(moves)+len(my_moves) >= 10:
                return max(set(moves), key=moves.count)
            if not moves[0]:
                return self.randomize()
            return self.randomize(9, 1)
        return True