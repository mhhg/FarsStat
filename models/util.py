from models import Cell, Column, Missing
from random import random

def fill_random():
    cells = [Cell(row, col, data=random() * 10000) for col in range(5) for row
             in range(10 ** 2)]
    for col in range(5):
        column = Column.get(col)
        column.name = "c{}".format(col)
        column.values["mamad"] = str(12)
        column.values["12"] = "mamad"
        column.missing = Missing()
