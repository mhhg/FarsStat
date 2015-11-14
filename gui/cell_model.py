from PyQt5.QtCore import QAbstractTableModel, Qt, QSize
from PyQt5.QtGui import QColor

from models import Row, Column, Cell, DataType, Selection
from gui import ColList

NUMBER_OF_ROWS = 10 ** 2 * 2
NUMBER_OF_COLS = 10
import logging
logger = logging.getLogger("FS")


class CellModel(QAbstractTableModel):
    Columns = NUMBER_OF_COLS
    Rows = NUMBER_OF_ROWS
    CellSize = QSize(30, 20)
    NumericCellAlign = Qt.AlignRight | Qt.AlignVCenter
    SelectedRowColor = QColor("lightblue")
    UnSelectedRowColor = QColor("red")
    RowSize = QSize(30, 20)
    ColumnSize = QSize(65, 20)
    CellFlags = Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def __init__(self, parent):
        super(CellModel, self).__init__(parent)

    def rowCount(self, QModelIndex_parent=None, *args, **kwargs):
        rows_count = Row.count()
        # logger.debug("rows_count={}".format(rows_count))
        return CellModel.Rows

    def columnCount(self, index=None, *args, **kwargs):
        columns_count = Column.count()

        # logger.debug("columns_count={}, CellModel.Columns={}"
        #              .format(columns_count, CellModel.Columns))

        # if CellModel.Columns - COL_OFFSET <= columns_count:
        # logger.debug("CellModel.Columns changed.")
        # CellModel.Columns = columns_count + COL_OFFSET
        # logger.debug("index.row={}, index.col={}".format(index.row(),
        #                                                  index.column()))
        # self.columnChange()

        # CellModel.Columns += 1

        return CellModel.Columns

    def data(self, index, role=None):
        # logger.debug("index={}, role={}".format(QModelIndex, role))
        row, column = index.row(), index.column()
        if role == Qt.DisplayRole:
            cell = Cell.get(row, column)
            return cell.data if cell else None

        if role == Qt.EditRole:
            cell = Cell.get(row, column)
            return str(cell.data) if cell else None

        if role == Qt.SizeHintRole:
            return CellModel.CellSize

        if role == Qt.TextAlignmentRole:
            column = Column.get(column)
            if column:
                if column.type.type == DataType.Numeric:
                    return CellModel.NumericCellAlign

    def setData(self, index, data, role=None):
        row, column = index.row(), index.column()
        cell = Cell.get(row, column)
        if not cell:
            if data:
                cell = Cell(row, column)
                cell.data = data
                self.headerDataChanged.emit(Qt.Horizontal, column,
                                            Qt.DisplayRole)
                ColList.List.reset()
        else:
            cell.data = data

        return True

    def headerData(self, id, orientation, role=None):
        if orientation == Qt.Horizontal:
            if role == Qt.ItemDataRole:
                return str(id)

            elif role == Qt.DisplayRole:
                column = Column.get(id)
                return column.name if column else "var"

            elif role == Qt.SizeHintRole:
                return CellModel.ColumnSize
        else:
            if role == Qt.ItemDataRole:
                return str(id)

            elif role == Qt.DisplayRole:
                return str(id + 1)

            elif role == Qt.TextAlignmentRole:
                return Qt.AlignCenter

            elif role == Qt.SizeHintRole:
                return CellModel.RowSize

            elif role == Qt.BackgroundRole:
                if Selection().is_selected(id):
                    return CellModel.SelectedRowColor
                else:
                    return CellModel.UnSelectedRowColor

    def flags(self, QModelIndex):
        return CellModel.CellFlags
