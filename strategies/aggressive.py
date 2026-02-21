from strategy import Strategy as Base

import random

class Strategy(Base):

    def __init__(self):
        self.name = "Aggressive"
        self.description = "Smart, but tends to betray"
        self.consecutive_false = 0
        self.last_consecutive = 0
        self.probed = False
        self.probe_check = False

    def randomize(self, true_odds: int = 3, false_odds: int = 7):
        return random.choices((True, False), [true_odds, false_odds])[0]

    def play(self, moves: list[bool] = None, my_moves: list[bool] = None):
        if moves:

            if not moves[0]:
                self.consecutive_false += 1

            if moves[0]:
                self.last_consecutive = self.consecutive_false
                if self.last_consecutive > 0:
                    self.last_consecutive = 0
                self.consecutive_false = 0

            if self.consecutive_false == 2:
                return False
            
            elif self.consecutive_false > 2:
                if not self.probed:
                    rand = self.randomize()
                    if rand:
                        self.probed = True

                if self.probe_check:
                    self.probed = False
                    self.probe_check = False
                    if moves[0]:
                        return self.randomize(true_odds=7-self.last_consecutive/4,false_odds=3+self.last_consecutive/4)
                    else:
                        return False

                if self.probed:
                    self.probe_check = True
                    return self.randomize(true_odds=7-self.last_consecutive/4,false_odds=3+self.last_consecutive/4)
                
            
            return self.randomize(true_odds=7-self.last_consecutive/4,false_odds=3+self.last_consecutive/4)
        
        return True