import logging

from PyQt5.QtWidgets import (QGroupBox, QRadioButton, QSpinBox, QLabel,
                             QGridLayout, QSizePolicy)
from PyQt5.QtCore import Qt

logger = logging.getLogger("FS")


class OldValuesWidget(QGroupBox):
    def __init__(self, parent):
        super(OldValuesWidget, self).__init__(parent)

        self.single_value = QRadioButton(self)
        self.value = QSpinBox(self)
        # self.system_missing = QRadioButton(self)
        # self.system_or_user_missing = QRadioButton(self)
        self.range = QRadioButton(self)
        self.range_from = QSpinBox(self)
        self.range_lbl = QLabel(self)
        self.range_to = QSpinBox(self)
        self.range_tl_rd = QRadioButton(self)
        self.range_tl_sb = QSpinBox(self)
        self.range_th_rd = QRadioButton(self)
        self.range_th_sb = QSpinBox(self)
        self.all_other = QRadioButton(self)

        self.grid = QGridLayout(self)
        self.ui()
        self.properties()
        # self.revert()
        self.events()

    def properties(self):
        self.setTitle("Old Values")
        self.single_value.setText("Value:")
        # self.system_missing.setText("System missing:")
        # self.system_or_user_missing.setText("System or user missing:")
        self.range.setText("Range:")
        self.range_lbl.setText("through")
        self.range_tl_rd.setText("LOWEST through value:")
        self.range_th_rd.setText("value through HIGHEST:")
        self.all_other.setText("All other values")
        self.single_value.setChecked(True)
        self.range_from.setEnabled(False)
        self.range_to.setEnabled(False)
        self.range_th_sb.setEnabled(False)
        self.range_tl_sb.setEnabled(False)

    def events(self):
        self.range.toggled.connect(self.range_toggled)
        self.range_tl_rd.toggled.connect(self.range_tl_rd_toggled)
        self.range_th_rd.toggled.connect(self.range_th_rd_toggled)
        self.single_value.toggled.connect(self.single_value_toggled)

    def single_value_toggled(self, event):
        self.value.setEnabled(event)

    def range_tl_rd_toggled(self, event):
        self.range_tl_sb.setEnabled(event)

    def range_th_rd_toggled(self, event):
        self.range_th_sb.setEnabled(event)

    def range_toggled(self, event):
        self.range_from.setEnabled(event)
        self.range_to.setEnabled(event)

    def ui(self):
        self.grid.addWidget(self.single_value, 0, 0, 1, 2)
        self.grid.addWidget(self.value, 0, 2, 1, 8)
        # self.grid.addWidget(self.system_missing, 1, 0, 1, 10)
        # self.grid.addWidget(self.system_or_user_missing, 2, 0, 1, 10)
        # self.grid.addWidget(self.system_missing, 3, 0, 1, 10)
        self.grid.addWidget(self.range, 4, 0, 1, 10)
        self.grid.addWidget(self.range_tl_rd, 5, 0, 1, 10)
        self.grid.addWidget(self.range_from, 6, 0, 1, 4)
        self.grid.addWidget(self.range_lbl, 6, 4, 1, 2, Qt.AlignHCenter)
        self.grid.addWidget(self.range_to, 6, 6, 1, 4)
        self.grid.addWidget(self.range_tl_rd, 9, 0, 1, 10)
        self.grid.addWidget(self.range_tl_sb, 10, 0, 1, 10)
        self.grid.addWidget(self.range_th_rd, 11, 0, 1, 10)
        self.grid.addWidget(self.range_th_sb, 12, 0, 1, 10)
        self.grid.addWidget(self.all_other, 13, 0, 1, 10)
        self.grid.setSpacing(1)
        self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Maximum)
