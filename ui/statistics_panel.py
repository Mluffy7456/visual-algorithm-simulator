from PySide6.QtWidgets import (
    QGroupBox,
    QLabel,
    QVBoxLayout,
    QWidget,
)

from config.language_manager import tr


class StatisticsPanel(QWidget):
    def __init__(self):
        super().__init__()

        self.comparisons_count = 0
        self.swaps_count = 0
        self.array_accesses_count = 0
        self.elapsed_time_value = 0.0

        self.build_ui()
        self.retranslate_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)

        self.group = QGroupBox()

        group_layout = QVBoxLayout()

        self.comparisons_label = QLabel()
        self.swaps_label = QLabel()
        self.array_accesses_label = QLabel()
        self.elapsed_time_label = QLabel()

        group_layout.addWidget(self.comparisons_label)
        group_layout.addWidget(self.swaps_label)
        group_layout.addWidget(self.array_accesses_label)
        group_layout.addWidget(self.elapsed_time_label)
        group_layout.addStretch()

        self.group.setLayout(group_layout)

        layout.addWidget(self.group)

    def update_statistics(
        self,
        comparisons,
        swaps,
        array_accesses=0,
        elapsed_time=0.0,
    ):
        self.comparisons_count = comparisons
        self.swaps_count = swaps
        self.array_accesses_count = array_accesses
        self.elapsed_time_value = elapsed_time

        self.retranslate_ui()

    def reset(self):
        self.update_statistics(
            0,
            0,
            0,
            0.0
        )

    def retranslate_ui(self):
        self.group.setTitle(
            tr("statistics")
        )

        self.comparisons_label.setText(
            f"{tr('comparisons')}: {self.comparisons_count}"
        )

        self.swaps_label.setText(
            f"{tr('swaps')}: {self.swaps_count}"
        )

        self.array_accesses_label.setText(
            f"{tr('array_accesses')}: {self.array_accesses_count}"
        )

        self.elapsed_time_label.setText(
            f"{tr('elapsed_time')}: {self.elapsed_time_value:.3f} s"
        )