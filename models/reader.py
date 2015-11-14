"""

with SavReader(savFileName, returnHeader=True) as reader:
        header = next(reader)
        for line in reader:
            process(line)
"""


class Reader(object):
    pass