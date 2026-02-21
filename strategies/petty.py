from strategy import Strategy as Base

import random

class Strategy(Base):

    def __init__(self):
        self.name = "Petty"
        self.description = "Holds grudges against you, does not forgive easily"
        self.aggravated = False
        self.last_true = False

    def randomize(self, true_odds: int = 1, false_odds: int = 9):
        return random.choices((True, False), [true_odds, false_odds])[0]

    def play(self, moves: list[bool] = None, my_moves: list[bool] = None):
        if moves:

            if not moves[0]:
                self.aggravated = True

            if self.last_true and moves[0]:
                self.aggravated = False

            if self.aggravated:
                rand = self.randomize()
                self.last_true = rand
                return rand
            
        return True