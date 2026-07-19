from algorithms.base.algorithm import Algorithm


class InsertionSort(Algorithm):
    name = "Insertion Sort"

    def __init__(self, canvas):
        super().__init__(canvas)

    def sort(self):
        values = self.canvas.values
        n = len(values)

        if n > 0:
            self.canvas.mark_sorted(0)

        for i in range(1, n):

            key = values[i]
            self.array_accesses += 1

            j = i - 1

            while j >= 0:

                self.canvas.highlight(j, j + 1)

                self.comparisons += 1
                self.array_accesses += 1

                yield

                if values[j] <= key:
                    break

                values[j + 1] = values[j]

                self.array_accesses += 2
                self.swaps += 1

                self.canvas.update()

                yield

                j -= 1

            values[j + 1] = key

            self.array_accesses += 1

            self.canvas.update()

            for k in range(i + 1):
                self.canvas.mark_sorted(k)

            yield

        self.canvas.clear_highlight()

        for i in range(n):
            self.canvas.mark_sorted(i)

        yield