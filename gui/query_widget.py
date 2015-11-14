from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

from models import Query, Selection, Row
from gui import QueryInput, ColorWidget, DataView


class QueryWidget(QWidget):
    def __init__(self, parent):
        super(QueryWidget, self).__init__(parent)

        self.input = QueryInput(self)

        self.lbl_color = QLabel(self)
        self.color = ColorWidget(self, Query.DefaultColor)
        self.exec = QPushButton(self)
        # self.history = QueryHistoryWidget(self)
        self.grid = QGridLayout(self)

        self.ui()
        self.properties()

        self.exec.clicked.connect(self.execute)

    def execute(self):
        # color = self.color.color.name(QtGui.QColor.HexRgb)
        query = Query(self.input.toPlainText())
        query.execute()
        if query.error == Query.NoError:
            selection = Selection()
            selection.query = query
            DataView.Model.headerDataChanged.emit(Qt.Vertical, 0, Row.count())

    def properties(self):
        self.input.setPlaceholderText("Query")
        self.lbl_color.setText("Color:")
        self.exec.setText("Execute")

    def ui(self):
        self.grid.addWidget(self.input, 0, 0, 1, 10)
        self.grid.addWidget(self.lbl_color, 1, 0, 1, 1, Qt.AlignRight)
        self.grid.addWidget(self.color, 1, 1, 0, 4)
        self.grid.addWidget(self.exec, 1, 5, 1, 5)
        # self.grid.addWidget(self.history, 2, 0, 1, 10)
