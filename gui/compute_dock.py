from PyQt5.QtWidgets import QDockWidget
from gui import ComputeWidget

class ComputeDock(QDockWidget):
    def __init__(self, parent):
        super(ComputeDock, self).__init__(parent)
        self.query = ComputeWidget(self)
        self.setWidget(self.query)
        self.setWindowTitle("Compute")
