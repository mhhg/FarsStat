import logging

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from models import Row
from gui import DataView
logger = logging.getLogger("FS")


class CaseRangeWidget(QGroupBox):
    def __init__(self, parent):
        super(CaseRangeWidget, self).__init__(parent)
        self.selection = self.parent().selection
        self.from_ = QSpinBox(self)
        self.to = QSpinBox(self)
        self.vbox = QVBoxLayout(self)
        self.ui()
        self.setTitle("Range")
        self.setDisabled(True)
        self.events()

    def ui(self):
        h1, h2 = QHBoxLayout(self), QHBoxLayout(self)
        observ = QLabel("Observation:")
        spacer = QSpacerItem(13, 0, QSizePolicy.Maximum, QSizePolicy.Maximum)
        first_lbl = QLabel("First Case")
        last_lbl = QLabel("Last Case")
        first_lbl.setFixedWidth(120)
        first_lbl.setAlignment(Qt.AlignRight)
        last_lbl.setAlignment(Qt.AlignLeft)
        h1.addWidget(first_lbl)
        h1.addSpacerItem(spacer)
        h1.addWidget(last_lbl, 100)

        h2.addWidget(observ, 0)
        h2.addWidget(self.from_, 1, Qt.AlignLeft)
        h2.addWidget(self.to, 100, Qt.AlignLeft)

        self.from_.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.to.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        self.from_.setFixedWidth(60)
        self.to.setFixedWidth(60)
        self.vbox.addLayout(h1)
        self.vbox.addLayout(h2)

    def events(self):
        self.from_.valueChanged.connect(self.from_changed)
        self.to.valueChanged.connect(self.to_changed)

    def from_changed(self, value):
        self.selection.range.from_ = value
        DataView.Model.headerDataChanged.emit(Qt.Vertical, 0, Row.count())
        logger.debug(value)

    def to_changed(self, value):
        self.selection.range.to = value
        DataView.Model.headerDataChanged.emit(Qt.Vertical, 0, Row.count())
        logger.debug(value)
