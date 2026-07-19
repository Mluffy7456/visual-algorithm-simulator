import sys

from PySide6.QtWidgets import QApplication

from config.language_manager import LanguageManager
from config.settings_manager import SettingsManager
from ui.main_window import MainWindow


def main():
    SettingsManager.load()
    LanguageManager.load()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()