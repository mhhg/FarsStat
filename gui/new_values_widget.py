from PyQt5.QtWidgets import (QGroupBox, QRadioButton, QSpinBox, QGridLayout,
                             QSizePolicy)
from PyQt5.QtCore import Qt


class NewValuesWidget(QGroupBox):
    def __init__(self, parent):
        super(NewValuesWidget, self).__init__(parent)

        self.new_rd = QRadioButton(self)
        self.new_sb = QSpinBox(self)
        self.system_missing = QRadioButton(self)
        self.copy_old_values = QRadioButton(self)
        self.grid = QGridLayout(self)

        self.ui()
        self.properties()

        self.new_rd.toggled.connect(self.new_rd_toggled)

    def new_rd_toggled(self, event):
        self.new_sb.setEnabled(event)

    def properties(self):
        self.setTitle("New Values")
        self.new_rd.setText("Value")
        self.system_missing.setText("System missing")
        self.copy_old_values.setText("Copy old values")

        self.new_rd.setChecked(True)

    def ui(self):
        self.grid.addWidget(self.new_rd, 0, 0, 1, 1, Qt.AlignTop)
        self.grid.addWidget(self.new_sb, 0, 1, 1, 9, Qt.AlignTop)
        self.grid.addWidget(self.system_missing, 1, 0, 1, 10, Qt.AlignTop)
        self.grid.addWidget(self.copy_old_values, 2, 0, 1, 10)
        self.grid.setSpacing(1)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
