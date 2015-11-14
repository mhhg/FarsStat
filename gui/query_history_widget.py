from PyQt5.QtWidgets import (QWidget, QGridLayout, QTreeView, QPushButton)

from models import Query
from gui import QueryListModel


class QueryHistoryWidget(QWidget):
    def __init__(self, parent):
        super(QueryHistoryWidget, self).__init__(parent)
        self.selected_query = None

        self.list = QTreeView(self)
        self.model = QueryListModel(self)
        self.re_exec = QPushButton(self)
        self.select = QPushButton(self)
        self.grid = QGridLayout(self)

        self.ui()
        self.properties()

    def execute(self):
        # color = self.color.color.name(QtGui.QColor.HexRgb)
        query = Query(self.input.toPlainText())
        query.execute()

    def properties(self):
        self.select.setText("Select")
        self.re_exec.setText("Re execute")

    def ui(self):
        self.grid.addWidget(self.list, 0, 0, 1, 10)
        self.grid.addWidget(self.select, 1, 0, 1, 1)
        self.grid.addWidget(self.re_exec, 1, 1, 1, 1)
        # self.grid.setContentsMargins(0, 0, 0, 0)
