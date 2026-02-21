from strategy import Strategy as Base

import random

class Strategy(Base):

    def __init__(self):
        self.name = "Random"
        self.description = "RANDOM BULLSHIT GO!!!"

    def play(self, moves: list[bool] = None, my_moves: list[bool] = None):
        return random.choice([True, False])