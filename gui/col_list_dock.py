from PyQt5 import QtWidgets
from gui import ColList

class ColListDock(QtWidgets.QDockWidget):
    def __init__(self, parent):
        super(ColListDock, self).__init__(parent)
        self.list_col = ColList(self)
        self.setWidget(self.list_col)
        self.setWindowTitle("Variables")

