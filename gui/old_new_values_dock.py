from PyQt5.QtWidgets import QDockWidget

from gui import OldNewValuesWidget


class OldNewValuesDock(QDockWidget):
    def __init__(self, parent):
        super(OldNewValuesDock, self).__init__(parent)
        self.old_new_values_widget = OldNewValuesWidget(self)
        self.setWidget(self.old_new_values_widget)
        self.setWindowTitle("Old New Values")
