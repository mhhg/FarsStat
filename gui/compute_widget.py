import logging

from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QLineEdit)

from models import Query, Column, Cell
from gui import QueryInput

logger = logging.getLogger("FS")


class ComputeWidget(QWidget):
    def __init__(self, parent):
        super(ComputeWidget, self).__init__(parent)

        self.input = QueryInput(self)
        self.exec = QPushButton(self)
        self.grid = QGridLayout(self)
        self.target = QLineEdit(self)
        self.ui()
        self.properties()

        self.exec.clicked.connect(self.execute)

    def execute(self):
        query = Query(select=self.input.toPlainText())
        query.execute()
        if query.error == Query.NoError:
            var_name = self.target.text().strip()
            column = None
            new_column = False
            if var_name:
                logger.debug("var_name={}".format(var_name))
                column = Column.get_by_name(var_name)

            if not column:
                column = Column(Column.count(), name=var_name)
                new_column = True

            logger.debug("new_column={}".format(new_column))

            for row, data in query.result.items():
                if new_column:
                    Cell(row, column.id, data=data)
                else:
                    cell = Cell.get(row, column.id)
                    cell.data = data

    def properties(self):
        self.input.setPlaceholderText("Query")
        self.exec.setText("Execute")
        self.target.setPlaceholderText("Target Variable")

    def ui(self):
        self.grid.addWidget(self.input, 1, 0, 1, 10)
        self.grid.addWidget(self.exec, 2, 5, 1, 5)
        self.grid.addWidget(self.target, 0, 0, 1, 10)

    def events(self):
        self.exec.clicked.connect(self.execute)
