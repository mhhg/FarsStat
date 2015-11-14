from PyQt5.QtWidgets import QDockWidget

from gui import QueryHistoryWidget

class QueryHistoryDock(QDockWidget):
    def __init__(self, parent):
        super(QueryHistoryDock, self).__init__(parent)
        self.query = QueryHistoryWidget(self)
        self.setWidget(self.query)
        self.setWindowTitle("Query History")
