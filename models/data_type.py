import models

class DataType(object):
    Numeric = 0
    Str = 1
    Date = 2
    Width = 8
    Decimal = 2
    Types = {
        Numeric: 'Numeric',
        Str: 'String',
        Date: 'Date'
    }

    DateFormat = {
        0: 'yyyy/MM/dd  HH:mm',
    }

    NumericFormat = '{:.2f}'

    def __init__(self, column_id, type=Numeric, width=Width,
                 decimal=Decimal, formatting=NumericFormat):
        self.column_id = column_id
        self._type = type
        self._width = width
        self._decimal = decimal
        self._formatting = formatting

    @property
    def column(self):
        return models.Column.get(self.column_id)

    @column.setter
    def column(self, column):
        self.column_id = column.id

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, data_type):
        self._type = data_type

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def decimal(self):
        return self._decimal

    @decimal.setter
    def decimal(self, value):
        self._decimal = value

    @property
    def formmating(self):
        return "{:" + ".{}f".format(self.decimal) + "}"

    @formmating.setter
    def formatting(self, value):
        self._formatting = value

    def __repr__(self):
        return "<DataType(column_id={}, type={}, width={}, decimal={})" \
            .format(self.column_id, self._type, self._width, self._decimal)
