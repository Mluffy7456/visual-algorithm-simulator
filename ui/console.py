from PySide6.QtWidgets import QTextEdit


class Console(QTextEdit):
    def __init__(self):
        super().__init__()

        self.setReadOnly(True)
        self.setMinimumHeight(180)

    def write(self, text):
        self.append(text)