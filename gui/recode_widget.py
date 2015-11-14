from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton,
                             QLineEdit, QCheckBox)
from PyQt5.QtCore import Qt

from models import Recode, Column


class RecodeWidget(QWidget):
    def __init__(self, parent):
        super(RecodeWidget, self).__init__(parent)

        self.old_var = QLineEdit(self)
        self.new_var = QLineEdit(self)
        self.recode = QPushButton(self)
        self.same = QCheckBox(self)
        self.old_new_values = QPushButton(self)
        self.grid = QGridLayout(self)

        self.ui()
        self.properties()

        self.recode.clicked.connect(self.execute)

        self.same.toggled.connect(self.same_toggled)

    def same_toggled(self, event):
        self.new_var.setEnabled(not event)

    def execute(self):
        if self.old_var.text().strip():
            old_column = Column.get_by_name(self.old_var.text().strip())
            new_column = None

            if self.same.isChecked():
                new_column = Column.get_by_name(self.new_var.text().strip())

            recode = Recode(old_column, new_column)
            recode.execute()

    def properties(self):
        self.old_var.setPlaceholderText("Old Variable")
        self.new_var.setPlaceholderText("New Variable")
        self.same.setText("Recode into same variable")
        self.recode.setText("Recode")
        self.old_new_values.setText("Old New Values")
        self.new_var.setEnabled(False)
        self.same.setChecked(True)

    def ui(self):
        self.grid.addWidget(self.old_var, 0, 0, 1, 10)
        self.grid.addWidget(self.same, 1, 0, 1, 10)
        self.grid.addWidget(self.new_var, 2, 0, 1, 10)
        self.grid.addWidget(self.recode, 3, 9, 1, 1, Qt.AlignBottom)
        self.grid.addWidget(self.old_new_values, 3, 8, 1, 1, Qt.AlignBottom)
