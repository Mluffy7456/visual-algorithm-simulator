from PySide6.QtCore import QObject, QTimer


class SimulationEngine(QObject):
    def __init__(self, canvas, console, statistics):
        super().__init__()

        self.canvas = canvas
        self.console = console
        self.statistics = statistics

        self.algorithm = None

        self.timer = QTimer()
        self.timer.timeout.connect(self.next_step)

        self.speed = 40

    # --------------------------------------------------

    def load_algorithm(self, algorithm):
        self.stop()

        self.algorithm = algorithm
        self.algorithm.reset()

        self.statistics.reset()

        self.console.clear()
        self.console.write(f"Loaded: {algorithm.name}")

    # --------------------------------------------------

    def start(self):
        if self.algorithm is None:
            self.console.write("Select an algorithm first.")
            return

        self.console.write("Simulation started.")

        interval = max(1, 101 - self.speed)

        self.timer.start(interval)

    # --------------------------------------------------

    def stop(self):
        self.timer.stop()

    # --------------------------------------------------

    def pause(self):
        self.timer.stop()
        self.console.write("Paused.")

    # --------------------------------------------------

    def reset(self):
        self.stop()

        self.canvas.generate_array()

        if self.algorithm:
            self.algorithm.reset()

        self.statistics.reset()

        self.console.clear()
        self.console.write("Array regenerated.")

    # --------------------------------------------------

    def set_speed(self, speed):
        self.speed = speed

        if self.timer.isActive():
            interval = max(1, 101 - speed)
            self.timer.start(interval)

    # --------------------------------------------------

    def update_statistics(self):
        if self.algorithm is None:
            return

        self.statistics.update_statistics(
            self.algorithm.comparisons,
            self.algorithm.swaps,
            self.algorithm.array_accesses,
            self.algorithm.elapsed_time,
        )

    # --------------------------------------------------

    def next_step(self):
        if self.algorithm is None:
            return

        finished = self.algorithm.step()

        self.update_statistics()

        if finished:
            self.stop()

            self.update_statistics()

            self.console.write("Finished.")