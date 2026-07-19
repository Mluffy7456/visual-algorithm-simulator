from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QLabel,
    QListWidget,
    QVBoxLayout,
    QWidget,
)


class SidePanel(QWidget):
    algorithm_selected = Signal(str)

    def __init__(self):
        super().__init__()

        self.setFixedWidth(250)

        self.build_ui()
        self.connect_signals()

    def build_ui(self):
        layout = QVBoxLayout(self)

        title = QLabel("Algorithms")
        title.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
        """)

        self.list = QListWidget()

        self.list.addItems([
            "Bubble Sort",
            "Selection Sort",
            "Insertion Sort",
        ])

        layout.addWidget(title)
        layout.addWidget(self.list)

    def connect_signals(self):
        self.list.currentTextChanged.connect(
            self.algorithm_selected.emit
        )

    def current_algorithm(self):
        return self.list.currentItem().text() if self.list.currentItem() else None