import logging

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from models import Row, RandomSample
from gui import DataView

logger = logging.getLogger("FS")


class RandomSampleWidget(QGroupBox):
    def __init__(self, parent):
        super(RandomSampleWidget, self).__init__(parent)
        self.selection = self.parent().selection

        self.approx = QRadioButton(self)
        self.exact = QRadioButton(self)
        self.approx_value = QSpinBox(self)
        self.exact_value = QSpinBox(self)
        self.from_value = QSpinBox(self)

        # self.grid = QGridLayout(self)
        self.vbox = QVBoxLayout(self)
        self.setDisabled(True)

        self.properties()
        self.ui()
        self.events()

    def ui(self):
        h1, h2, h3 = QHBoxLayout(self), QHBoxLayout(self), QHBoxLayout(self)
        h1.addWidget(self.approx)
        h1.addWidget(self.approx_value, 0, Qt.AlignLeft)
        h1.addWidget(QLabel("% of all cases"), 1, Qt.AlignLeft)
        h2.addWidget(self.exact, 0)
        h2.addWidget(self.exact_value, 100, Qt.AlignLeft)
        h3.addWidget(QLabel("case from the first"))
        h3.addWidget(self.from_value)
        h3.addWidget(QLabel("cases"), 100)

        self.vbox.addLayout(h1)
        self.vbox.addLayout(h2)
        self.vbox.addLayout(h3)
        # h1.setContentsMargins(0, 0, 0, 0)
        # h2.setContentsMargins(0, 0, 0, 0)
        self.approx_value.setSizePolicy(QSizePolicy.Maximum,
                                        QSizePolicy.Maximum)
        self.exact_value.setSizePolicy(QSizePolicy.Maximum,
                                       QSizePolicy.Maximum)
        self.from_value.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        # self.vbox.setContentsMargins(1, 10, 1, 10)
        # self.vbox.setSpacing(2)

    def properties(self):
        self.setTitle("Sample Size")
        self.approx.setText("Approximately")
        self.exact.setText("Exactly")

    def events(self):
        self.approx_value.valueChanged.connect(self.approx_changed)
        self.exact_value.valueChanged.connect(self.exact_changed)
        self.from_value.valueChanged.connect(self.from_changed)
        self.approx.clicked.connect(self.approx_type_checked)
        self.exact.clicked.connect(self.exact_type_checked)

    def approx_type_checked(self, event):
        self.revert()
        self.selection.random_sample.type = RandomSample.Approximately
        self.set()

    def exact_type_checked(self, event):
        self.revert()
        self.selection.random_sample.type = RandomSample.Exactly
        self.set()

    def approx_changed(self, value):
        self.selection.random_sample.percent = value
        DataView.Model.headerDataChanged.emit(Qt.Vertical, 0, Row.count())
        logger.debug(value)

    def exact_changed(self, value):
        self.selection.random_sample.no = value
        DataView.Model.headerDataChanged.emit(Qt.Vertical, 0, Row.count())
        logger.debug(value)

    def from_changed(self, value):
        self.selection.random_sample.from_ = value
        DataView.Model.headerDataChanged.emit(Qt.Vertical, 0, Row.count())
        logger.debug(value)

    def revert(self):
        self.approx_value.setValue(0)
        self.exact_value.setValue(0)
        self.from_value.setValue(0)
        self.approx.setAutoExclusive(False)
        self.exact.setAutoExclusive(False)
        self.approx.setChecked(False)
        self.exact.setChecked(False)
        self.approx.clearMask()
        self.exact.clearMask()
        self.approx.setAutoExclusive(True)
        self.exact.setAutoExclusive(True)

        self.repaint()

    def set(self):
        self.selection = self.parent().selection
        if self.selection.random_sample.type == RandomSample.Approximately:
            self.approx.setChecked(True)
        else:
            self.exact.setChecked(True)

        self.approx_value.setValue(self.selection.random_sample.percent)
        self.exact_value.setValue(self.selection.random_sample.no)
        self.from_value.setValue(self.selection.random_sample.from_)
