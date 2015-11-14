
class Row(object):
    Height = 20
    Max = 10 ** 5
    DefaultColor = "cornsilk"
    array = {}

    def __init__(self, id):
        # logger.debug("Row: {} instantiated.".format(id))
        self._id = id
        Row.array[id] = self

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    def __repr__(self):
        return "<Row(id={})>".format(self.id)

    @classmethod
    def get(cls, item):
        if item in Row.array:
            return Row.array[item]

    @classmethod
    def count(cls):
        return len(Row.array)

