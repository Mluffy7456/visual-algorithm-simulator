from algorithms.sorting.bubble_sort import BubbleSort
from algorithms.sorting.selection_sort import SelectionSort
from algorithms.sorting.insertion_sort import InsertionSort


class AlgorithmManager:
    def __init__(self):
        self._algorithms = {}

        self.register("Bubble Sort", BubbleSort)
        self.register("Selection Sort", SelectionSort)
        self.register("Insertion Sort", InsertionSort)

    def register(self, name, algorithm_class):
        self._algorithms[name] = algorithm_class

    def create(self, name, canvas):
        algorithm = self._algorithms.get(name)

        if algorithm is None:
            return None

        return algorithm(canvas)

    def names(self):
        return sorted(self._algorithms.keys())

    def exists(self, name):
        return name in self._algorithms