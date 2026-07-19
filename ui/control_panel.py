from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSlider,
    QWidget,
)


class ControlPanel(QWidget):
    start_clicked = Signal()
    pause_clicked = Signal()
    step_clicked = Signal()
    reset_clicked = Signal()
    generate_clicked = Signal()

    speed_changed = Signal(int)

    def __init__(self):
        super().__init__()

        self.build_ui()
        self.connect_signals()

    def build_ui(self):
        layout = QHBoxLayout(self)

        self.generate_button = QPushButton("Generate")
        self.start_button = QPushButton("Start")
        self.pause_button = QPushButton("Pause")
        self.step_button = QPushButton("Step")
        self.reset_button = QPushButton("Reset")

        self.speed_label = QLabel("Speed")

        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(1, 100)
        self.speed_slider.setValue(40)
        self.speed_slider.setFixedWidth(180)

        layout.addWidget(self.generate_button)
        layout.addWidget(self.start_button)
        layout.addWidget(self.pause_button)
        layout.addWidget(self.step_button)
        layout.addWidget(self.reset_button)

        layout.addStretch()

        layout.addWidget(self.speed_label)
        layout.addWidget(self.speed_slider)

    def connect_signals(self):
        self.generate_button.clicked.connect(
            self.generate_clicked.emit
        )

        self.start_button.clicked.connect(
            self.start_clicked.emit
        )

        self.pause_button.clicked.connect(
            self.pause_clicked.emit
        )

        self.step_button.clicked.connect(
            self.step_clicked.emit
        )

        self.reset_button.clicked.connect(
            self.reset_clicked.emit
        )

        self.speed_slider.valueChanged.connect(
            self.speed_changed.emit
        )