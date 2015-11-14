from collections import OrderedDict
import logging

from models import DataType, Missing

logger = logging.getLogger("FS")


class Column(object):
    array = {}
    Width = 400
    Max = 10 ** 2

    AlignBaseline = 256
    AlignBottom = 64
    AlignCenter = 132
    AlignHCenter = 4
    AlignJustify = 8
    AlignLeft = 1
    AlignRight = 2
    AlignTop = 32
    AlignVCenter = 128

    def __init__(self, id, name=None):
        self._id = id
        # logger.debug("Column: {} instantiated.".format(id))
        self._name = name if name else "VAR {}".format(str(id).zfill(5))
        self.data_type = DataType(self.id)
        self.label = ""
        self.values = OrderedDict()
        self.missing = Missing()

        if id > Column.count():
            for i in range(Column.count(), id):
                logger.debug("creating column automatically. col={}".format(i))
                Column(i)

        Column.array[id] = self

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            self._name = value
        else:
            self._name = "VAR {}".format(str(self.id).zfill(5))

    @property
    def type(self):
        return self.data_type

    @type.setter
    def type(self, value):
        self.data_type = value

    def __repr__(self):
        return "<Column(id={}, name={})>".format(self.id, self.name)

    @classmethod
    def get(cls, id):
        if id in Column.array:
            return Column.array[id]

    @classmethod
    def get_by_name(cls, name):
        logger.debug(Column.array.items())
        columns = filter(lambda column: column.name == name,
                         Column.array.values())
        columns = list(columns)
        if columns:
            return columns[0]

    @classmethod
    def names_list(cls):
        return [Column.get(id).name if id in Column.array else "" for id in
                range(Column.count())]

    @classmethod
    def data_types_list(self):
        names = Column.names_list()
        return {name: 0 for name in names}

    @classmethod
    def count(cls):
        return len(Column.array)
