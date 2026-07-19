from algorithms.base.algorithm import Algorithm


class BubbleSort(Algorithm):
    name = "Bubble Sort"

    def __init__(self, canvas):
        super().__init__(canvas)

    def sort(self):
        values = self.canvas.values
        n = len(values)

        for i in range(n):

            swapped = False

            for j in range(n - i - 1):

                self.canvas.highlight(j, j + 1)

                self.comparisons += 1
                yield

                if values[j] > values[j + 1]:

                    self.canvas.swap(j, j + 1)

                    self.swaps += 1
                    swapped = True

                    yield

            self.canvas.mark_sorted(n - i - 1)

            yield

            if not swapped:
                break

        self.canvas.clear_highlight()

        for i in range(n):
            self.canvas.mark_sorted(i)

        yield