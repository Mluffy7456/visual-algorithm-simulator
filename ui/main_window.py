from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from algorithms.algorithm_manager import AlgorithmManager
from config.language_manager import (
    LanguageManager,
    tr,
)
from config.settings_manager import SettingsManager
from core.simulation_engine import SimulationEngine
from graphics.canvas import Canvas
from ui.console import Console
from ui.control_panel import ControlPanel
from ui.dialogs.settings_window import SettingsWindow
from ui.side_panel import SidePanel
from ui.statistics_panel import StatisticsPanel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.manager = AlgorithmManager()

        self.build_ui()
        self.connect_signals()
        self.apply_settings()

    def build_ui(self):
        self.setWindowTitle(tr("app_name"))

        self.resize(
            SettingsManager.get("window.width", 1600),
            SettingsManager.get("window.height", 900)
        )

        central = QWidget()
        self.setCentralWidget(central)

        root = QHBoxLayout(central)
        root.setContentsMargins(10, 10, 10, 10)
        root.setSpacing(10)

        # ---------- Левая панель ----------

        self.side_panel = SidePanel()

        # ---------- Центр ----------

        self.canvas = Canvas()
        self.control_panel = ControlPanel()

        center_layout = QVBoxLayout()
        center_layout.setSpacing(10)

        center_layout.addWidget(self.canvas)
        center_layout.addWidget(self.control_panel)

        # ---------- Правая панель ----------

        self.statistics = StatisticsPanel()
        self.console = Console()

        right_layout = QVBoxLayout()
        right_layout.setSpacing(10)

        right_layout.addWidget(self.statistics)
        right_layout.addWidget(self.console)

        # ---------- Engine ----------

        self.engine = SimulationEngine(
            self.canvas,
            self.console,
            self.statistics,
        )

        # ---------- Layout ----------

        root.addWidget(self.side_panel)
        root.addLayout(center_layout, 1)
        root.addLayout(right_layout)

    def connect_signals(self):
        self.side_panel.algorithm_selected.connect(
            self.load_algorithm
        )

        if hasattr(self.side_panel, "settings_clicked"):
            self.side_panel.settings_clicked.connect(
                self.open_settings
            )

        self.control_panel.start_clicked.connect(
            self.engine.start
        )

        self.control_panel.pause_clicked.connect(
            self.engine.pause
        )

        self.control_panel.step_clicked.connect(
            self.engine.next_step
        )

        self.control_panel.reset_clicked.connect(
            self.engine.reset
        )

        self.control_panel.generate_clicked.connect(
            self.canvas.generate_array
        )

        self.control_panel.speed_changed.connect(
            self.engine.set_speed
        )

    def load_algorithm(self, name):
        algorithm = self.manager.create(
            name,
            self.canvas,
        )

        if algorithm is None:
            return

        self.engine.load_algorithm(algorithm)

    def open_settings(self):
        dialog = SettingsWindow(self)

        if dialog.exec():
            LanguageManager.set_language(
                SettingsManager.get("language")
            )

            self.apply_settings()

    def apply_settings(self):
        self.setWindowTitle(
            tr("app_name")
        )

        self.engine.set_speed(
            SettingsManager.get(
                "animation.speed",
                40
            )
        )

        if hasattr(self.side_panel, "retranslate_ui"):
            self.side_panel.retranslate_ui()

        if hasattr(self.control_panel, "retranslate_ui"):
            self.control_panel.retranslate_ui()

        if hasattr(self.statistics, "retranslate_ui"):
            self.statistics.retranslate_ui()

        if hasattr(self.console, "retranslate_ui"):
            self.console.retranslate_ui()

        if SettingsManager.get(
            "window.fullscreen",
            False
        ):
            self.showFullScreen()