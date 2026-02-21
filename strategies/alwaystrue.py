from strategy import Strategy as Base

class Strategy(Base):

    def __init__(self):
        self.name = "Always True"
        self.description = "Always cooperates"

    def play(self, moves: list[bool] = None, my_moves: list[bool] = None):
        return True