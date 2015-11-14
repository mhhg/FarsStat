from PyQt5 import QtWidgets

from gui import ColumnListModel
import gui
from models import Column


class ColList(QtWidgets.QWidget):
    List = None
    Model = None

    def __init__(self, parent):
        super(ColList, self).__init__(parent)
        self.cols = QtWidgets.QTreeView(self)
        self.cols_model = ColumnListModel(self)
        ColList.Model = self.cols_model
        ColList.List = self.cols
        self.cols.setModel(self.cols_model)

        self.grid = QtWidgets.QGridLayout(self)
        self.grid.addWidget(self.cols, 0, 0, 5, 10)
        self.cols.doubleClicked.connect(self.double_click)
        self.properties()
        self.ui()

    def double_click(self, index):
        column = Column.get(index.row())
        gui.ColChange.instance.set(column) if column else None

    def properties(self):
        self.cols.setRootIsDecorated(False)
        self.cols.resizeColumnToContents(0)
        self.cols.resizeColumnToContents(1)
        self.cols.resizeColumnToContents(2)
        self.cols.resizeColumnToContents(3)
        self.cols.resizeColumnToContents(4)
        self.cols.resizeColumnToContents(5)

    def ui(self):
        pass
