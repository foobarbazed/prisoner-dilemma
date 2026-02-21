class Strategy:

    def __init__(self):
        self.name = "base strategy"
        self.description = "The base strategy for all strategies"

    def play(self, moves: list[bool] = None, my_moves: list[bool] = None):
        return True