import traceback
import math


class Variance():
    def varc(self, data, average):
        var = 0.00
        try:
            for i in range(0, len(data)):
                var += (average - data[i]) ** 2
            if len(data) > 0:
                return var / (len(data) - 1)
            else:
                return "No data is available"
        except:
            return traceback.format_exc()