import logging

from models import OldNewValue, Cell

logger = logging.getLogger("FS")


class Recode(object):
    array = {}

    def __init__(self, old_column, new_column=None):
        self.id = len(Recode.array)

        self.old_column = old_column
        self.new_column = new_column

    def execute(self):
        old_new_values = OldNewValue.all()
        # onv = old new value
        for onv in old_new_values.values():

            if onv.type == OldNewValue.SingleValue \
                    or onv.type == OldNewValue.Range:

                for cell in Cell.get_by_value(onv.old1):
                    cell.data = onv.new
