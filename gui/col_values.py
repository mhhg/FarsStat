from PyQt5.QtWidgets import *


class ColValues(QGroupBox):
    def __init__(self, parent):
        super(ColValues, self).__init__(parent)

        self.column = parent.column
        self.value = QLineEdit(self)
        self.label = QLineEdit(self)
        self.items = QTreeWidget(self)

        self.add = QPushButton(self)
        self.remove = QPushButton(self)
        self.change = QPushButton(self)
        self.grid = QGridLayout(self)

        self.properties()
        self.ui()
        self.events()

    def add_value(self, event):
        label = self.label.text()
        value = self.value.text()
        if label and value:
            self.column.values[value] = label
            self.value.clear()
            self.label.clear()
            self.set()

    def remove_value(self, evnet):
        item = self.items.selectedItems()
        if item:
            item = item[0]
            value = item.data(0, 0)
            self.column.values.pop(value)
            self.set()

    def change_value(self, event):
        item = self.items.selectedItems()
        if item:
            item = item[0]
            value = item.data(0, 0)
            label = item.data(1, 0)
            self.value.setText(value)
            self.label.setText(label)
            self.column.values.pop(value)
            self.set()

    def events(self):
        self.add.clicked.connect(self.add_value)
        self.remove.clicked.connect(self.remove_value)
        self.change.clicked.connect(self.change_value)

    def properties(self):
        self.setTitle("Values")
        self.value.setPlaceholderText("Value")
        self.label.setPlaceholderText("Label")
        self.items.setColumnCount(2)
        self.items.setHeaderLabels(["Value", "Label"])
        self.add.setText("Add")
        self.remove.setText("Remove")
        self.change.setText("Change")
        self.items.setRootIsDecorated(False)

    def ui(self):
        self.add.setMaximumWidth(50)
        self.remove.setMaximumWidth(50)
        self.change.setMaximumWidth(50)
        self.grid.addWidget(self.value, 0, 0, 1, 5)
        self.grid.addWidget(self.label, 0, 5, 1, 5)
        self.grid.addWidget(self.items, 1, 0, 4, 9)
        self.grid.addWidget(self.add, 1, 9, 1, 1)
        self.grid.addWidget(self.change, 2, 9, 1, 1)
        self.grid.addWidget(self.remove, 3, 9, 1, 1)
        self.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)

    def set(self):
        self.column = self.parent().column
        if self.column:
            self.items.clear()
            for value, label in self.column.values.items():
                item = QTreeWidgetItem([str(value), str(label)])
                self.items.addTopLevelItem(item)
