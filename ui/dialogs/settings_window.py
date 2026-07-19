from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDialog,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSlider,
    QVBoxLayout,
)

from config.language_manager import tr
from config.settings_manager import SettingsManager


class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle(tr("settings"))
        self.setMinimumWidth(500)

        self.build_ui()
        self.load_settings()

    def build_ui(self):
        layout = QVBoxLayout(self)

        # ---------------- Appearance ----------------

        appearance_group = QGroupBox(tr("appearance"))
        appearance_layout = QFormLayout()

        self.theme_box = QComboBox()
        self.theme_box.addItem(tr("dark"), "dark")
        self.theme_box.addItem(tr("light"), "light")

        self.language_box = QComboBox()
        self.language_box.addItem("English", "en")
        self.language_box.addItem("Русский", "ru")

        appearance_layout.addRow(
            QLabel(tr("theme")),
            self.theme_box
        )

        appearance_layout.addRow(
            QLabel(tr("language")),
            self.language_box
        )

        appearance_group.setLayout(appearance_layout)

        # ---------------- Animation ----------------

        animation_group = QGroupBox(tr("animation"))
        animation_layout = QFormLayout()

        self.array_slider = QSlider(Qt.Horizontal)
        self.array_slider.setRange(10, 300)

        self.speed_slider = QSlider(Qt.Horizontal)
        self.speed_slider.setRange(1, 100)

        animation_layout.addRow(
            QLabel(tr("array_size")),
            self.array_slider
        )

        animation_layout.addRow(
            QLabel(tr("animation_speed")),
            self.speed_slider
        )

        animation_group.setLayout(animation_layout)

        # ---------------- Interface ----------------

        interface_group = QGroupBox(tr("information"))

        interface_layout = QVBoxLayout()

        self.legend_checkbox = QCheckBox(
            tr("show_legend")
        )

        self.statistics_checkbox = QCheckBox(
            tr("show_statistics")
        )

        self.algorithm_checkbox = QCheckBox(
            tr("show_algorithm_info")
        )

        self.explanation_checkbox = QCheckBox(
            tr("show_step_explanation")
        )

        self.console_checkbox = QCheckBox(
            tr("show_console")
        )

        self.sound_checkbox = QCheckBox(
            tr("play_sounds")
        )

        interface_layout.addWidget(self.legend_checkbox)
        interface_layout.addWidget(self.statistics_checkbox)
        interface_layout.addWidget(self.algorithm_checkbox)
        interface_layout.addWidget(self.explanation_checkbox)
        interface_layout.addWidget(self.console_checkbox)
        interface_layout.addWidget(self.sound_checkbox)

        interface_group.setLayout(interface_layout)

        # ---------------- Buttons ----------------

        buttons = QHBoxLayout()

        buttons.addStretch()

        cancel_button = QPushButton(
            tr("cancel")
        )

        save_button = QPushButton(
            tr("save")
        )

        cancel_button.clicked.connect(self.reject)
        save_button.clicked.connect(self.save_settings)

        buttons.addWidget(cancel_button)
        buttons.addWidget(save_button)

        # ---------------- Layout ----------------

        layout.addWidget(appearance_group)
        layout.addWidget(animation_group)
        layout.addWidget(interface_group)
        layout.addStretch()
        layout.addLayout(buttons)

    def load_settings(self):
        self.theme_box.setCurrentIndex(
            0 if SettingsManager.get("theme") == "dark" else 1
        )

        self.language_box.setCurrentIndex(
            0 if SettingsManager.get("language") == "en" else 1
        )

        self.array_slider.setValue(
            SettingsManager.get("array.size")
        )

        self.speed_slider.setValue(
            SettingsManager.get("animation.speed")
        )

        self.legend_checkbox.setChecked(
            SettingsManager.get("interface.show_legend")
        )

        self.statistics_checkbox.setChecked(
            SettingsManager.get("interface.show_statistics")
        )

        self.algorithm_checkbox.setChecked(
            SettingsManager.get("interface.show_algorithm_info")
        )

        self.explanation_checkbox.setChecked(
            SettingsManager.get(
                "interface.show_step_explanation"
            )
        )

        self.console_checkbox.setChecked(
            SettingsManager.get("interface.show_console")
        )

        self.sound_checkbox.setChecked(
            SettingsManager.get("sound.enabled")
        )

    def save_settings(self):
        SettingsManager.set(
            "theme",
            self.theme_box.currentData()
        )

        SettingsManager.set(
            "language",
            self.language_box.currentData()
        )

        SettingsManager.set(
            "array.size",
            self.array_slider.value()
        )

        SettingsManager.set(
            "animation.speed",
            self.speed_slider.value()
        )

        SettingsManager.set(
            "interface.show_legend",
            self.legend_checkbox.isChecked()
        )

        SettingsManager.set(
            "interface.show_statistics",
            self.statistics_checkbox.isChecked()
        )

        SettingsManager.set(
            "interface.show_algorithm_info",
            self.algorithm_checkbox.isChecked()
        )

        SettingsManager.set(
            "interface.show_step_explanation",
            self.explanation_checkbox.isChecked()
        )

        SettingsManager.set(
            "interface.show_console",
            self.console_checkbox.isChecked()
        )

        SettingsManager.set(
            "sound.enabled",
            self.sound_checkbox.isChecked()
        )

        SettingsManager.save()

        self.accept()