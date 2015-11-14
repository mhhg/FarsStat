from PyQt5 import QtWidgets
from PyQt5 import QtCore
from models import Missing

class ColMissing(QtWidgets.QGroupBox):
    def __init__(self, parent):
        super(ColMissing, self).__init__(parent)
        self.column = self.parent().column

        self.no = QtWidgets.QRadioButton(self)
        self.discrete = QtWidgets.QRadioButton(self)
        self.range = QtWidgets.QRadioButton(self)

        self.min = QtWidgets.QSpinBox(self)
        self.max = QtWidgets.QSpinBox(self)
        self.range_discrete = QtWidgets.QSpinBox(self)
        self.discrete1 = QtWidgets.QSpinBox(self)
        self.discrete2 = QtWidgets.QSpinBox(self)
        self.discrete3 = QtWidgets.QSpinBox(self)

        self.lbl_min = QtWidgets.QLabel(self)
        self.lbl_max = QtWidgets.QLabel(self)
        self.lbl_range_discrete = QtWidgets.QLabel(self)

        self.grid = QtWidgets.QGridLayout(self)
        self.properties()
        self.ui()
        self.events()

    def properties(self):
        self.setTitle("Missing values")
        self.no.setText("No Missing Values")
        self.discrete.setText("Discrete Missing Values")
        self.range.setText("Range plus one optional value")
        self.lbl_min.setText("Low:")
        self.lbl_max.setText("High:")
        self.lbl_range_discrete.setText("Discrete:")

    def ui(self):
        self.grid.addWidget(self.no, 0, 0, 1, 6)
        self.grid.addWidget(self.discrete, 1, 0, 1, 6)
        self.grid.addWidget(self.discrete1, 2, 0, 1, 2)
        self.grid.addWidget(self.discrete2, 2, 2, 1, 2)
        self.grid.addWidget(self.discrete3, 2, 4, 1, 2)
        self.grid.addWidget(self.range, 3, 0, 1, 6)
        self.grid.addWidget(self.lbl_min, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.grid.addWidget(self.min, 4, 1, 1, 1)
        self.grid.addWidget(self.lbl_max, 4, 2, 1, 1, QtCore.Qt.AlignRight)
        self.grid.addWidget(self.max, 4, 3, 1, 1)
        self.grid.addWidget(self.lbl_range_discrete, 4, 4, 1, 1,
                            QtCore.Qt.AlignRight)
        self.grid.addWidget(self.range_discrete, 4, 5, 1, 1)
        self.setSizePolicy(QtWidgets.QSizePolicy.Maximum,
                           QtWidgets.QSizePolicy.Maximum)

    def set(self):
        self.column = self.parent().column
        if self.column:
            self.discrete1.setDisabled(True)
            self.discrete2.setDisabled(True)
            self.discrete3.setDisabled(True)
            self.min.setDisabled(True)
            self.max.setDisabled(True)
            self.range_discrete.setDisabled(True)

            if self.column.missing.type == Missing.No:
                self.no.setChecked(True)

            elif self.column.missing.type == Missing.Discrete:
                self.discrete1.setEnabled(True)
                self.discrete2.setEnabled(True)
                self.discrete3.setEnabled(True)
                self.discrete1.setValue(self.column.missing.n1)
                self.discrete2.setValue(self.column.missing.n2)
                self.discrete3.setValue(self.column.missing.n3)

            elif self.column.missing.type == Missing.Range:
                self.min.setEnabled(True)
                self.max.setEnabled(True)
                self.range_discrete.setEnabled(True)
                self.min.setValue(self.column.missing.n1)
                self.max.setValue(self.column.missing.n2)
                self.range_discrete.setValue(self.column.missing.n3)

    def events(self):
        self.no.clicked.connect(self.no_changed)
        self.discrete.clicked.connect(self.discrete_changed)
        self.range.clicked.connect(self.range_changed)
        self.discrete1.valueChanged.connect(self.discrete1_changed)
        self.discrete2.valueChanged.connect(self.discrete2_changed)
        self.discrete3.valueChanged.connect(self.discrete3_changed)

        self.min.valueChanged.connect(self.min_changed)
        self.max.valueChanged.connect(self.max_changed)
        self.range_discrete.valueChanged.connect(self.range_discrete_changed)

    def no_changed(self, event):
        self.column.missing.type = Missing.No
        self.set()

    def discrete_changed(self, event):
        self.column.missing.type = Missing.Discrete
        self.column.missing.n1 = self.discrete1.value()
        self.column.missing.n2 = self.discrete2.value()
        self.column.missing.n3 = self.discrete3.value()
        self.set()

    def range_changed(self, event):
        self.column.missing.type = Missing.Range
        self.column.missing.n1 = self.min.value()
        self.column.missing.n2 = self.max.value()
        self.column.missing.n3 = self.range_discrete.value()
        self.set()

    def discrete1_changed(self, value):
        self.column.missing.n1 = value

    def discrete2_changed(self, value):
        self.column.missing.n2 = value

    def discrete3_changed(self, value):
        self.column.missing.n3 = value

    def min_changed(self, value):
        self.column.missing.n1 = value

    def max_changed(self, value):
        self.column.missing.n2 = value

    def range_discrete_changed(self, value):
        self.column.missing.n3 = value

