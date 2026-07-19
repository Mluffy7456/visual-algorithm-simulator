import random

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter
from PySide6.QtWidgets import QWidget


class Canvas(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(800, 600)

        self.values = []

        self.active_indexes = set()
        self.sorted_indexes = set()

        self.default_color = QColor("#3b82f6")
        self.active_color = QColor("#ef4444")
        self.sorted_color = QColor("#22c55e")

        self.generate_array()

    # -------------------------
    # Работа с массивом
    # -------------------------

    def generate_array(self, size=60):
        self.values = [
            random.randint(20, 500)
            for _ in range(size)
        ]

        self.clear_highlight()
        self.update()

    def set_array(self, values):
        self.values = list(values)
        self.clear_highlight()
        self.update()

    # -------------------------
    # Подсветка
    # -------------------------

    def highlight(self, *indexes):
        self.active_indexes = set(indexes)
        self.update()

    def mark_sorted(self, index):
        self.sorted_indexes.add(index)
        self.update()

    def clear_highlight(self):
        self.active_indexes.clear()
        self.sorted_indexes.clear()
        self.update()

    # -------------------------
    # Изменение массива
    # -------------------------

    def swap(self, first, second):
        self.values[first], self.values[second] = (
            self.values[second],
            self.values[first],
        )

        self.update()

    def set_value(self, index, value):
        self.values[index] = value
        self.update()

    # -------------------------
    # Отрисовка
    # -------------------------

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)

        painter.fillRect(self.rect(), QColor("#1e1e1e"))

        if not self.values:
            return

        width = self.width()
        height = self.height()

        count = len(self.values)

        spacing = 2
        bar_width = width / count

        maximum = max(self.values)

        for i, value in enumerate(self.values):

            bar_height = value / maximum * (height - 20)

            x = int(i * bar_width)
            y = int(height - bar_height)

            color = self.default_color

            if i in self.sorted_indexes:
                color = self.sorted_color

            elif i in self.active_indexes:
                color = self.active_color

            painter.fillRect(
                x,
                y,
                int(bar_width - spacing),
                int(bar_height),
                color,
            )