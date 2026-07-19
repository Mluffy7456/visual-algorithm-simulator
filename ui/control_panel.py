from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSlider,
    QWidget,
)

from config.language_manager import tr
from config.settings_manager import SettingsManager


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
        self.retranslate_ui()

    def build_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        self.generate_button = QPushButton()
        self.start_button = QPushButton()
        self.pause_button = QPushButton()
        self.step_button = QPushButton()
        self.reset_button = QPushButton()

        self.speed_label = QLabel()

        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(1, 100)
        self.speed_slider.setFixedWidth(180)

        self.speed_slider.setValue(
            SettingsManager.get(
                "animation.speed",
                40
            )
        )

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

        self.speed_slider.valueChanged.connect(
            self.save_speed
        )

    def save_speed(self, value):
        SettingsManager.set(
            "animation.speed",
            value
        )

        SettingsManager.save()

    def retranslate_ui(self):
        self.generate_button.setText(
            "🎲 " + tr("generate")
        )

        self.start_button.setText(
            "▶ " + tr("start")
        )

        self.pause_button.setText(
            "⏸ " + tr("pause")
        )

        self.step_button.setText(
            "⏭ " + tr("step")
        )

        self.reset_button.setText(
            "⟲ " + tr("reset")
        )

        self.speed_label.setText(
            tr("animation_speed")
        )