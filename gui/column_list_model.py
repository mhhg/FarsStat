import logging

from PyQt5 import QtCore
from PyQt5.QtCore import Qt

from models import DataType, Column

logger = logging.getLogger("FS")


class ColumnListModel(QtCore.QAbstractTableModel):
    ColumnsCount = 5
    Name = 0
    Type = 1
    Width = 2
    Decimal = 3
    Label = 4

    headers = {
        Name: "Name",
        Type: "Type",
        Width: "Width",
        Decimal: "Decimal",
        Label: "Label",
    }

    item_data = {
        Name: lambda column: column.name,
        Type: lambda column: DataType.Types[column.type.type],
        Width: lambda column: column.type.width,
        Decimal: lambda column: column.type.decimal,
        Label: lambda column: column.label,
    }

    item_size = {
        Name: 80,
        Type: 60,
        Width: 40,
        Decimal: 50,
        Label: 90,
    }

    item_alignment = {
        Name: Qt.AlignLeft,
        Type: Qt.AlignCenter,
        Width: Qt.AlignCenter,
        Decimal: Qt.AlignCenter,
        Label: Qt.AlignLeft,
    }

    def __init__(self, parent):
        super(ColumnListModel, self).__init__(parent)

    def columnCount(self, *args, **kwargs):
        return ColumnListModel.ColumnsCount

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return Column.count()

    def data(self, index, role=None):
        row, col = index.row(), index.column()
        if role == Qt.DisplayRole:
            column = Column.get(row)
            if column:
                return ColumnListModel.item_data[col](column)
            else:
                logger.debug("Column not found. column_id={}".format(row))
        if role == Qt.SizeHintRole:
            return QtCore.QSize(ColumnListModel.item_size[col], 15)
        if role == Qt.TextAlignmentRole:
            return ColumnListModel.item_alignment[col]

    def headerData(self, id, orientation, role=None):
        if role == Qt.ItemDataRole:
            return str(id)
        if role == Qt.DisplayRole:
            return ColumnListModel.headers[id]
        if role == Qt.SizeHintRole:
            return QtCore.QSize(20, 20)
        if role == Qt.TextAlignmentRole:
            return ColumnListModel.item_alignment[id]
