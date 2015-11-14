import traceback

__author__ = 'sara'


class ArithMean():
    def mean(self, data):
        try:
            m = sum(data) / len(data)
            return m
        except:
            return traceback.format_exc()


