import logging

from models import Column, Row, DataType, db

logger = logging.getLogger("FS")


class Cell(object):
    array = {}

    def __init__(self, row, column, data=None):
        self.id = len(Cell.array)
        self.row_id = row
        self.column_id = column
        self._data = data

        column_obj = Column.get(column)
        row_obj = Row.get(row)

        if not self.column:
            self.column = Column(column)
        else:
            self.column = column_obj

        if not self.row:
            self.row = Row(row)
        else:
            self.row = row_obj

        Cell.array[(row, column)] = self

    @property
    def row(self):
        return Row.get(self.row_id)

    @row.setter
    def row(self, row):
        self.row_id = row.id

    @property
    def data(self):
        if self.column.type.type == DataType.Numeric:
            try:
                return self.column.type.formatting.format(float(self._data)) \
                    .zfill(self.column.type.width)
            except ValueError:
                logger.debug("Invalid value={} "
                             "for cell={}".format(self._data, self))
                return "?"
        elif self.column.type.type == DataType.Str:
            return self._data

    @data.setter
    def data(self, value):
        if self.column.type.type == DataType.Numeric:
            try:
                self._data = float(value)
                logger.debug(float(value))
            except ValueError:
                logger.debug(
                    "Invalid value={} for cell={}".format(value, self))
        else:
            self._data = value

    @property
    def column(self):
        return Column.get(self.column_id)

    @column.setter
    def column(self, column):
        self.column_id = column.id

    @classmethod
    def get(cls, row, col):
        item = (row, col)
        if item in Cell.array:
            return Cell.array[item]

    @classmethod
    def get_by_value(cls, value):
        ret = None
        if isinstance(value, (str, int, float)):
            ret = filter(lambda cell: cell.data == value, Cell.array.values())
        elif isinstance(value, range):
            ret = filter(lambda cell: cell.data in value, Cell.array.values())

        return ret

    @classmethod
    def to_records(cls):
        columns = Column.count()
        rows = Row.count()

        return [[str(Cell.array[(row, column)]._data)
                 if (row, column) in Cell.array else ""
                 for column in range(columns)] for row in range(rows)]

    @classmethod
    def create_table(cls):
        db.execute("CREATE TABLE IF NOT EXISTS cells ("
                   "id INTEGER PRIMARY KEY NOT NULL,"
                   "row INTEGER NOT NULL,"
                   "column INTEGER NOT NULL,"
                   "data REAL)")

    @classmethod
    def insert(cls):
        db.execute("DROP TABLE IF EXISTS cells")
        Cell.create_table()
        cells = [(cell.id, cell.row_id, cell.column_id, cell._data)
                 for key, cell in Cell.array.items()]
        db.executemany("INSERT INTO cells VALUES (?, ?, ?, ?)", cells)

    def __repr__(self):
        return "<Cell(id={}, row_id={}, col_id={}, data={})>" \
            .format(self.id, self.row_id, self.column_id, self._data)
