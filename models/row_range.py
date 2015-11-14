import logging

from core import Singleton

logger = logging.getLogger("FS")


class RowRange(object, metaclass=Singleton):
    def __init__(self, from_index=0, to_index=0):
        self._from = from_index
        self._to = to_index
        self.selection = []

    @property
    def from_(self):
        return self._from

    @from_.setter
    def from_(self, value):
        self._from = value
        self.execute()

    @property
    def to(self):
        return self._to

    @to.setter
    def to(self, value):
        self._to = value
        self.execute()

    def execute(self):
        logger.debug("execute called")
        try:
            self.selection = range(self._from, self._to)
        except Exception as e:
            logger.debug(e)
