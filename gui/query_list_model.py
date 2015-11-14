import logging

from PyQt5.QtCore import QAbstractTableModel, Qt, QSize

from PyQt5.QtGui import QColor

from models import Query

logger = logging.getLogger("FS")


class QueryListModel(QAbstractTableModel):
    Columns = 3
    CellSize = QSize(30, 20)
    NumericCellAlign = Qt.AlignRight | Qt.AlignVCenter
    SelectedRowColor = QColor("lightblue")
    UnSelectedRowColor = QColor("red")
    RowSize = QSize(30, 20)
    ColumnSize = QSize(65, 20)
    CellFlags = Qt.ItemIsEnabled | Qt.ItemIsSelectable
    Id = 0
    Input = 1
    Status = 2
    Returned = 3
    Labels = {
        Id: "ID",
        Input: "Input",
        Status: "Status",
        Returned: "Returned",
    }

    def __init__(self, parent):
        super(QueryListModel, self).__init__(parent)

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        return Query.count()

    def columnCount(self, index=None, *args, **kwargs):
        return QueryListModel.Columns

    def data(self, index, role=None):
        # logger.debug("index={}, role={}".format(QModelIndex, role))
        row, column = index.row(), index.column()

        if role == Qt.DisplayRole:
            query = Query.get(row)
            if query:
                if column == QueryListModel.Id:
                    return str(query.id)
                if column == QueryListModel.Input:
                    return str(query.input)
                if column == QueryListModel.Status:
                    return query.status_label
                if column == QueryListModel.Returned:
                    return str(len(query.result))

        # if role == Qt.EditRole:
        #     cell = Cell.get(row, column)
        #     return str(cell.data) if cell else None

        if role == Qt.SizeHintRole:
            return QueryListModel.CellSize

        if role == Qt.BackgroundRole:
            return QueryListModel.SelectedRowColor

    def headerData(self, id, orientation, role=None):
        if orientation == Qt.Horizontal:
            if role == Qt.ItemDataRole:
                return str(id)

            elif role == Qt.DisplayRole:
                return QueryListModel.Labels[id]

            elif role == Qt.SizeHintRole:
                return QueryListModel.ColumnSize

    def flags(self, QModelIndex):
        return QueryListModel.CellFlags
