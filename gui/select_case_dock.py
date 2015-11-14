from PyQt5.QtWidgets import *
from gui import SelectCaseWidget

class SelectCaseDock(QDockWidget):
    def __init__(self, parent):
        super(SelectCaseDock, self).__init__(parent)
        self.widget = SelectCaseWidget(self)
        self.setWidget(self.widget)
        self.setWindowTitle("Select Case")
