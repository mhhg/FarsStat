from PyQt5.QtWidgets import QDockWidget
from gui import QueryWidget

class QueryDock(QDockWidget):
    def __init__(self, parent):
        super(QueryDock, self).__init__(parent)
        self.query = QueryWidget(self)
        self.setWidget(self.query)
        self.setWindowTitle("Select Case")
