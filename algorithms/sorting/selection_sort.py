from algorithms.base.algorithm import Algorithm


class SelectionSort(Algorithm):
    name = "Selection Sort"

    def __init__(self, canvas):
        super().__init__(canvas)

    def sort(self):
        values = self.canvas.values
        n = len(values)

        for i in range(n):

            minimum = i

            for j in range(i + 1, n):

                self.canvas.highlight(minimum, j)

                self.comparisons += 1
                self.array_accesses += 2

                yield

                if values[j] < values[minimum]:

                    self.array_accesses += 2

                    minimum = j

                    self.canvas.highlight(minimum, j)

                    yield

                else:
                    self.array_accesses += 2

            if minimum != i:

                self.canvas.swap(i, minimum)

                self.swaps += 1
                self.array_accesses += 4

                yield

            self.canvas.mark_sorted(i)

            yield

        self.canvas.clear_highlight()

        for i in range(n):
            self.canvas.mark_sorted(i)

        yield