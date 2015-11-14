from core import Singleton
from models import RowRange, RandomSample
import logging

logger = logging.getLogger("FS")

class Selection(object, metaclass=Singleton):
    All = 0
    IfCondition = 1
    CaseRange = 2
    RandomSample = 3
    FilterVariable = 4

    def __init__(self):
        self.type = Selection.All
        self.filter_variable = None
        self.query = None
        self.range = RowRange()
        self.random_sample = RandomSample()

    def is_selected(self, row):
        if self.type == Selection.All:
            return True

        if self.type == Selection.CaseRange and row in self.range.selection:
            logger.debug("row: {} is selected. case range ".format(row))
            return True

        if self.type == Selection.IfCondition:
            if self.query:
                if row in self.query.result:
                    logger.debug(
                        "row: {} is selected. if condition ".format(row))
                    return True

        if self.type == Selection.RandomSample and row in \
                self.random_sample.selection:
            logger.debug("row: {} is selected. case random sample ".format(row))
            return True

        return False
