import logging

logger = logging.getLogger("FS")


class OldNewValue(object):
    array = {}

    RangeThroughLowest = 1
    RangeThroughHighest = 2
    Range = 3
    SingleValue = 4
    AllOtherValues = 5

    def __init__(self, id=None, old1=None, old2=None, new=None,
                 type=SingleValue):
        self.id = id if id else OldNewValue.count()
        self.old1 = old1

        if not (old1 or new):
            raise ValueError("at least one old and one new value must given.")

        self.old2 = old2
        self.new = new
        self.type = type

        OldNewValue.array[id] = self

    @classmethod
    def count(cls):
        return len(OldNewValue.array)

    @classmethod
    def all(cls):
        return OldNewValue.array
