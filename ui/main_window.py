from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

from algorithms.algorithm_manager import AlgorithmManager
from core.simulation_engine import SimulationEngine
from graphics.canvas import Canvas
from ui.console import Console
from ui.control_panel import ControlPanel
from ui.side_panel import SidePanel
from ui.statistics_panel import StatisticsPanel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Visual Algorithm Simulator")
        self.resize(1600, 900)

        self.manager = AlgorithmManager()

        self.build_ui()
        self.connect_signals()

    def build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)

        root = QHBoxLayout(central)
        root.setContentsMargins(10, 10, 10, 10)
        root.setSpacing(10)

        # Левая панель
        self.side_panel = SidePanel()

        # Центр
        self.canvas = Canvas()

        self.control_panel = ControlPanel()

        center_layout = QVBoxLayout()
        center_layout.setSpacing(10)

        center_layout.addWidget(self.canvas)
        center_layout.addWidget(self.control_panel)

        # Правая панель
        self.statistics = StatisticsPanel()
        self.console = Console()

        right_layout = QVBoxLayout()
        right_layout.setSpacing(10)

        right_layout.addWidget(self.statistics)
        right_layout.addWidget(self.console)

        # Ядро приложения
        self.engine = SimulationEngine(
            self.canvas,
            self.console,
            self.statistics,
        )

        root.addWidget(self.side_panel)
        root.addLayout(center_layout, 1)
        root.addLayout(right_layout)

    def connect_signals(self):
        self.side_panel.algorithm_selected.connect(
            self.load_algorithm
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