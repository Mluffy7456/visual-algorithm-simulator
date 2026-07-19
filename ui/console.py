from PySide6.QtWidgets import (
    QGroupBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from config.language_manager import tr


class Console(QWidget):
    def __init__(self):
        super().__init__()

        self.build_ui()
        self.retranslate_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.group = QGroupBox()

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setMinimumHeight(180)

        group_layout = QVBoxLayout()
        group_layout.addWidget(self.text_edit)

        self.group.setLayout(group_layout)

        layout.addWidget(self.group)

    def write(self, text):
        self.text_edit.append(text)

    def clear(self):
        self.text_edit.clear()

    def retranslate_ui(self):
        self.group.setTitle(
            tr("console")
        )