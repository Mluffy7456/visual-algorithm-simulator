import time


class Algorithm:
    name = "Algorithm"

    def __init__(self, canvas):
        self.canvas = canvas

        self.generator = None

        self.reset()

    def reset(self):
        self.comparisons = 0
        self.swaps = 0
        self.array_accesses = 0

        self.start_time = None
        self.elapsed_time = 0.0

        self.generator = self.sort()

    def step(self):
        if self.start_time is None:
            self.start_time = time.perf_counter()

        try:
            next(self.generator)
            return False

        except StopIteration:
            self.finish()
            return True

    def finish(self):
        if self.start_time is not None:
            self.elapsed_time = (
                time.perf_counter() - self.start_time
            )

    # --------------------------------------------------
    # Statistics helpers
    # --------------------------------------------------

    def read(self, index):
        self.array_accesses += 1
        return self.canvas.array[index]

    def write(self, index, value):
        self.array_accesses += 1
        self.canvas.array[index] = value

    def compare(self, left, right):
        self.array_accesses += 2
        self.comparisons += 1

        return (
            self.canvas.array[left]
            >
            self.canvas.array[right]
        )

    def compare_values(self, a, b):
        self.comparisons += 1
        return a > b

    def swap(self, i, j):
        self.array_accesses += 4
        self.swaps += 1

        self.canvas.array[i], self.canvas.array[j] = (
            self.canvas.array[j],
            self.canvas.array[i]
        )

    def sort(self):
        raise NotImplementedError