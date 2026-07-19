from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)


class StatisticsPanel(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        self.comparisons = QLabel("Comparisons: 0")
        self.swaps = QLabel("Swaps: 0")

        layout.addWidget(self.comparisons)
        layout.addWidget(self.swaps)
        layout.addStretch()

    def update_statistics(self, comparisons, swaps):
        self.comparisons.setText(
            f"Comparisons: {comparisons}"
        )

        self.swaps.setText(
            f"Swaps: {swaps}"
        )

    def reset(self):
        self.update_statistics(0, 0)