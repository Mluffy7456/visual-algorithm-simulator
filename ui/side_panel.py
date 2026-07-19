from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from config.language_manager import tr


class SidePanel(QWidget):
    algorithm_selected = Signal(str)
    settings_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.setFixedWidth(280)

        self.build_ui()
        self.retranslate_ui()
        self.connect_signals()

    def build_ui(self):
        layout = QVBoxLayout(self)

        self.title = QLabel()
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setStyleSheet("""
            QLabel{
                font-size:20px;
                font-weight:bold;
            }
        """)

        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)

        self.settings_button = QPushButton()

        layout.addWidget(self.title)
        layout.addWidget(self.tree)
        layout.addStretch()
        layout.addWidget(self.settings_button)

        self.populate_tree()

    def populate_tree(self):
        self.tree.clear()

        # ---------- Sorting ----------

        sorting = QTreeWidgetItem([
            tr("sorting")
        ])

        sorting.addChild(
            QTreeWidgetItem([tr("bubble_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("selection_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("insertion_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("merge_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("quick_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("heap_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("shell_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("cocktail_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("comb_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("gnome_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("odd_even_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("counting_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("radix_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("bucket_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("cycle_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("pancake_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("tim_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("stooge_sort")])
        )

        sorting.addChild(
            QTreeWidgetItem([tr("bogo_sort")])
        )

        self.tree.addTopLevelItem(sorting)

        # ---------- Searching ----------

        self.tree.addTopLevelItem(
            QTreeWidgetItem([
                tr("searching")
            ])
        )

        # ---------- Graph ----------

        self.tree.addTopLevelItem(
            QTreeWidgetItem([
                tr("graph")
            ])
        )

        # ---------- Trees ----------

        self.tree.addTopLevelItem(
            QTreeWidgetItem([
                tr("trees")
            ])
        )

        # ---------- Dynamic ----------

        self.tree.addTopLevelItem(
            QTreeWidgetItem([
                tr("dynamic")
            ])
        )

        # ---------- Geometry ----------

        self.tree.addTopLevelItem(
            QTreeWidgetItem([
                tr("geometry")
            ])
        )

        self.tree.expandAll()

    def connect_signals(self):
        self.tree.itemClicked.connect(
            self.item_clicked
        )

        self.settings_button.clicked.connect(
            self.settings_clicked.emit
        )

    def item_clicked(self, item, column):
        if item.childCount() != 0:
            return

        self.algorithm_selected.emit(
            item.text(0)
        )

    def current_algorithm(self):
        item = self.tree.currentItem()

        if item is None:
            return None

        if item.childCount():
            return None

        return item.text(0)

    def retranslate_ui(self):
        self.title.setText(
            tr("algorithms")
        )

        self.settings_button.setText(
            "⚙ " + tr("settings")
        )

        self.populate_tree()