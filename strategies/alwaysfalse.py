from strategy import Strategy as Base

class Strategy(Base):

    def __init__(self):
        self.name = "Always False"
        self.description = "Always betrays"

    def play(self, moves: list[bool] = None, my_moves: list[bool] = None):
        return False