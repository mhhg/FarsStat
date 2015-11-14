from PyQt5.QtWidgets import QDockWidget

from gui import RecodeWidget


class RecodeDock(QDockWidget):
    def __init__(self, parent):
        super(RecodeDock, self).__init__(parent)
        self.query = RecodeWidget(self)
        self.setWidget(self.query)
        self.setWindowTitle("Recode")
