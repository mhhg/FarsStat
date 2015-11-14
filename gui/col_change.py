import logging

from PyQt5 import QtWidgets

from PyQt5 import QtCore

from models import Column
from gui import ColGeneralAttributes
from gui import ColValues
from gui import ColMissing

logger = logging.getLogger("FS")


class ColChange(QtWidgets.QWidget):
    instance = None

    def __init__(self, parent):
        super(ColChange, self).__init__(parent)
        self.column = Column.get(0)

        self.general_attributes = ColGeneralAttributes(self)
        self.values = ColValues(self)
        self.missing = ColMissing(self)
        self.vbox = QtWidgets.QVBoxLayout(self)
        # self.vbox.setContentsMargins(0, 0, 0, 0)

        self.vbox.addWidget(self.general_attributes, QtCore.Qt.AlignTop)
        self.vbox.addWidget(self.values, QtCore.Qt.AlignTop)
        self.vbox.addWidget(self.missing, QtCore.Qt.AlignTop)
        # self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

        self.set(self.column)
        ColChange.instance = self

    def set(self, col):
        self.column = col
        logger.debug(self.column)
        self.general_attributes.set()
        self.values.set()
        self.missing.set()

    def selection(self):
        print('selection')

    def clear(self):
        self.general_attributes.clear()
