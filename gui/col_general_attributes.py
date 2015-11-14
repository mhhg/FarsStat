import logging

from PyQt5.QtWidgets import (QGroupBox, QLineEdit, QComboBox, QSpinBox,
                             QGridLayout, QSizePolicy)
from PyQt5.QtCore import Qt

from models import DataType, Column
from gui import DataView, ColList
logger = logging.getLogger("FS")


class ColGeneralAttributes(QGroupBox):
    def __init__(self, parent):
        super(ColGeneralAttributes, self).__init__(parent)

        self.column = parent.column

        self.name = QLineEdit(self)
        self.types = QComboBox(self)
        self.width = QSpinBox(self)
        self.decimal = QSpinBox(self)
        self.label = QLineEdit(self)
        self.date_format = QComboBox(self)

        self.grid = QGridLayout(self)

        self.ui()
        self.properties()
        self.events()

    def events(self):
        self.name.returnPressed.connect(self.name_changed)
        self.width.valueChanged.connect(self.width_changed)
        self.decimal.valueChanged.connect(self.decimal_changed)
        self.label.returnPressed.connect(self.label_changed)
        self.types.currentIndexChanged.connect(self.type_changed)

    def name_changed(self):
        name = self.name.text()
        self.column.name = name
        self.name.setText(self.column.name)
        self.update_data_view()

    def label_changed(self):
        label = self.label.text()
        self.column.label = label
        self.label.setText(self.column.label)
        self.update_data_view()

    def width_changed(self, width):
        self.column.type.width = width
        self.width.setValue(self.column.type.width)
        self.update_data_view()

    def decimal_changed(self, decimal):
        self.column.type.decimal = decimal
        self.decimal.setValue(self.column.type.decimal)
        self.update_data_view()

    def type_changed(self, type):
        self.column.type.type = type
        self.update_data_view()

    def update_data_view(self):
        args = Qt.Horizontal, self.column.id, Qt.DisplayRole
        DataView.Model.headerDataChanged.emit(*args)
        self.update_columns_list()

    def update_columns_list(self):
        begin = ColList.Model.createIndex(0, 0)
        end = ColList.Model.createIndex(0, Column.count())
        ColList.Model.dataChanged.emit(begin, end)

    def ui(self):
        self.grid.addWidget(self.name, 0, 0, 1, 10)
        self.grid.addWidget(self.types, 1, 0, 1, 7)
        self.grid.addWidget(self.width, 1, 7, 1, 3)
        self.grid.addWidget(self.date_format, 2, 0, 1, 7)
        self.grid.addWidget(self.decimal, 2, 7, 1, 3)
        self.grid.addWidget(self.label, 3, 0, 1, 10)
        self.grid.setAlignment(Qt.AlignTop)
        self.setSizePolicy(QSizePolicy.Preferred,
                           QSizePolicy.Maximum)

    def properties(self):
        self.setTitle("General Attributes")
        self.name.setPlaceholderText('Name')
        self.label.setPlaceholderText('Label')

        for value, name in DataType.Types.items():
            self.types.addItem(name, value)

        self.date_format.setEnabled(False)
        self.defaults()

    def defaults(self):
        self.width.setValue(DataType.Width)
        self.decimal.setValue(DataType.Decimal)

    def set(self):
        col = self.column = self.parent().column
        if col:
            logger.debug(self.column)
            self.name.setText(str(col.name))
            self.width.setValue(int(col.type.width))
            self.decimal.setValue(int(col.type.decimal))
            self.types.setCurrentIndex(int(col.type.type))
            self.label.setText(str(col.label))

    def clear(self):
        self.name.clear()
        self.types.setCurrentIndex(DataType.Numeric)
        self.defaults()
