from PyQt5.QtWidgets import QTextEdit

class QueryInput(QTextEdit):
    def __init__(self, parent):
        super(QueryInput, self).__init__(parent)
