from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from models import Selection, Row
from gui import RandomSampleWidget, CaseRangeWidget, DataView


class SelectCaseWidget(QWidget):
    def __init__(self, parent):
        super(SelectCaseWidget, self).__init__(parent)
        self.selection = Selection()

        self.all = QRadioButton(self)
        self.random_sample = QRadioButton(self)
        self.if_condition = QRadioButton(self)
        self.filter_variable = QRadioButton(self)

        self.if_condition_btn = QPushButton(self)
        self.random_sample_widget = RandomSampleWidget(self)
        self.case_range = QRadioButton(self)
        self.case_range_widget = CaseRangeWidget(self)
        self.filter_variable_line = QLineEdit(self)

        self.grid = QGridLayout(self)
        self.properties()
        self.ui()

        self.all.setChecked(True)
        self.if_condition_btn.setDisabled(True)
        self.filter_variable_line.setDisabled(True)
        self.events()

    def properties(self):
        self.all.setText("All Cases")
        self.random_sample.setText("Random sample of cases")
        self.case_range.setText("Based on time or case range")
        self.if_condition.setText("If condition is satisfied")
        self.filter_variable.setText("Use filter variable")
        self.if_condition_btn.setText("If Condition")

    def ui(self):
        self.grid.addWidget(self.all, 0, 0, 1, 6)
        self.grid.addWidget(self.if_condition, 1, 0, 1, 2)
        self.grid.addWidget(self.if_condition_btn, 1, 2, 1, 4, Qt.AlignLeft)
        self.grid.addWidget(self.random_sample, 3, 0, 1, 6)
        self.grid.addWidget(self.random_sample_widget, 4, 0, 2, 6)
        self.grid.addWidget(self.case_range, 6, 0, 1, 6)
        self.grid.addWidget(self.case_range_widget, 7, 0, 2, 6)
        self.grid.addWidget(self.filter_variable, 9, 0, 1, 6)
        self.grid.addWidget(self.filter_variable_line, 10, 0, 1, 6)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        # self.grid.setContentsMargins(2, 2, 2, 2)

    def events(self):
        self.all.clicked.connect(self.all_checked)
        self.random_sample.clicked.connect(self.random_sample_checked)
        self.if_condition.clicked.connect(self.if_condition_checked)
        self.case_range.clicked.connect(self.case_range_checked)
        self.filter_variable.clicked.connect(self.filter_variable_checked)
        self.if_condition_btn.clicked.connect(self.if_condition_clicked)

    def if_condition_clicked(self, event):
        query_widget.parent().raise_()

    def revert(self):
        self.random_sample_widget.setDisabled(True)
        self.case_range_widget.setDisabled(True)
        self.if_condition_btn.setDisabled(True)
        self.filter_variable_line.setDisabled(True)
        self.random_sample_widget.revert()
        # begin = data_view.cell_model.createIndex(0, 0)
        # end = data_view.cell_model.createIndex(100, 10)
        DataView.Model.headerDataChanged.emit(Qt.Vertical, 0, Row.count())

    def all_checked(self, event):
        self.revert()
        self.selection.type = Selection.All

    def random_sample_checked(self, event):
        self.revert()
        self.selection.type = Selection.RandomSample
        self.random_sample_widget.setEnabled(True)
        self.random_sample_widget.set()

    def if_condition_checked(self, event):
        self.revert()
        self.selection.type = Selection.IfCondition
        self.if_condition_btn.setEnabled(True)

    def case_range_checked(self, event):
        self.revert()
        self.selection.type = Selection.CaseRange
        self.case_range_widget.setEnabled(True)

    def filter_variable_checked(self, event):
        self.revert()
        self.selection.type = Selection.FilterVariable
        self.filter_variable_line.setEnabled(True)
