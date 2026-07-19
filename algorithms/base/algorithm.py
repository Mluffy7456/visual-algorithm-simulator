class Algorithm:
    name = "Algorithm"

    def __init__(self, canvas):
        self.canvas = canvas

        self.comparisons = 0
        self.swaps = 0

        self.generator = None

        self.reset()

    def reset(self):
        self.comparisons = 0
        self.swaps = 0

        self.generator = self.sort()

    def step(self):
        try:
            next(self.generator)
            return False
        except StopIteration:
            return True

    def sort(self):
        raise NotImplementedError