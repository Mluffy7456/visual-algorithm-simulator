from algorithms.sorting.bubble_sort import BubbleSort
from algorithms.sorting.insertion_sort import InsertionSort
from algorithms.sorting.selection_sort import SelectionSort


class AlgorithmManager:
    def __init__(self):
        self._algorithms = {
            BubbleSort.name: BubbleSort,
            SelectionSort.name: SelectionSort,
            InsertionSort.name: InsertionSort,
        }

    def create(self, name, canvas):
        algorithm_class = self._algorithms.get(name)

        if algorithm_class is None:
            return None

        return algorithm_class(canvas)

    def names(self):
        return list(self._algorithms.keys())

    def register(self, algorithm_class):
        self._algorithms[algorithm_class.name] = algorithm_class