from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QSizePolicy, QListWidget,
                             QPushButton, QGridLayout)

from gui import OldValuesWidget, NewValuesWidget


class OldNewValuesWidget(QWidget):
    def __init__(self, parent):
        super(OldNewValuesWidget, self).__init__(parent)

        self.old_widget = OldValuesWidget(self)
        self.new_widget = NewValuesWidget(self)
        self.list = QListWidget(self)
        self.add = QPushButton(self)
        self.remove = QPushButton(self)
        self.grid = QGridLayout(self)

        self.ui()
        self.add.setText("Add")
        self.remove.setText("Remove")

    def ui(self):
        self.grid.addWidget(self.old_widget, 0, 0, 1, 3)
        self.grid.addWidget(self.new_widget, 1, 0, 1, 3, Qt.AlignTop)
        self.grid.addWidget(self.list, 2, 0, 10, 3)
        self.grid.addWidget(self.add, 12, 0, 1, 1)
        self.grid.addWidget(self.remove, 12, 1, 1, 1)
        self.setSizePolicy(QSizePolicy.MinimumExpanding,
                           QSizePolicy.Expanding)
