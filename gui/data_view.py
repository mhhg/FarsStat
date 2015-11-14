import logging

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *

from gui import CellModel

logger = logging.getLogger("FS")


class DataView(QtWidgets.QTableView):
    Model = None

    def __init__(self, parent):
        super(DataView, self).__init__(parent)
        self.cell_model = CellModel(self)
        DataView.Model = self.cell_model
        self.setModel(self.cell_model)
        self.resizeRowsToContents()
        self.resizeColumnsToContents()
        # self.setSelectionMode(QTableView.SelectRows)
        # self.setSelectionMode(QTableView.MultiSelection)
        # self.setSelectionModel()
        self.setSelectionBehavior(QTableView.SelectItems)

        # self.selectionChanged.connect(self.selectionChanged_)

        # def selectionChanged(self, begin, end):
        #     self.clearSelection()
        # logger.debug("selection changed")
        # return None

    def clicked_(self, index):
        logger.debug(
            "index.row={}, index.col={}".format(index.row(), index.column()))
        row, column = index.row(), index.column()
        if column > CellModel.Columns - 2:
            self.addColumns()

        if row > CellModel.Rows - 2:
            self.addRows()

    def addColumns(self):
        logger.debug("attempt to add columns. CellModel.Column={}".format(
            CellModel.Columns))
        # self.createIndex()
        # self.cell_model.beginInsertColumns()

    def addRows(self):
        logger.debug("attempt to add rows")
