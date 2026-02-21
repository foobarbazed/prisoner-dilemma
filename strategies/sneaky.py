from strategy import Strategy as Base

import random

class Strategy(Base):

    def __init__(self):
        self.name = "Sneaky"
        self.description = "Eye for an Eye, but can sabotage"
        self.success = 0

    def randomize(self, true_odds: float = 9, false_odds: float = 1):
        return random.choices((True, False), [true_odds, false_odds])[0]

    def play(self, moves: list[bool] = None, my_moves: list[bool] = None):
        if moves:
            if moves[0]:
                self.success += 1
                return self.randomize(true_odds=9-self.success/2, false_odds=1+self.success/2)
            else:
                self.success = 0
                return False
        return self.randomize()