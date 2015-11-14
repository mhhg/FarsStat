from PyQt5 import QtWidgets

from gui import ColChange


class ColChangeDock(QtWidgets.QDockWidget):
    def __init__(self, parent):
        super(ColChangeDock, self).__init__(parent)
        self.change_col = ColChange(self)
        self.setWidget(self.change_col)
        self.setWindowTitle("Variable Properties")
