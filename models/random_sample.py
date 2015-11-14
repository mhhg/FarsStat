import logging
from random import sample
from core import Singleton
from models import Row

logger = logging.getLogger("FS")


class RandomSample(object, metaclass=Singleton):
    Approximately = 1
    Exactly = 2

    def __init__(self, type=Exactly):
        self._type = type
        self._percent = 0
        self._from = 0
        self._no = 0
        self.selection = []

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value
        self.execute()

    @property
    def percent(self):
        return self._percent

    @percent.setter
    def percent(self, value):
        if 0 < value < 100:
            self._percent = value
            self.execute()

    @property
    def from_(self):
        return self._from

    @from_.setter
    def from_(self, value):
        self._from = value
        self.execute()

    @property
    def no(self):
        return self._no

    @no.setter
    def no(self, value):
        self._no = value
        self.execute()

    def execute(self):
        r = Row.count()
        approx, exact = RandomSample.Approximately, RandomSample.Exactly
        try:
            if r > 0:
                if self.type == approx:
                    args = range(0, r), int(r * self.percent / 100)

                elif self.type == exact:
                    args = range(0, self._from), self.no
                # print(*args)
                # print("r={}".format(r))
                self.selection = sample(*args)
        except ValueError as e:
            logger.error(e)
