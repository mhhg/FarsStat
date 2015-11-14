__author__ = 'sara'

import math


class ZScore():
    def __init__(self):
        pass

    def z_value(self, ave, std_d, data):
        zv = (data - ave) / std_d
        return zv

    def z_score(self, mean, sd, value):
        zv = self.z_value(mean, sd, value)
        # mean=2.75
        a = abs(zv)
        if zv == 0.0:
            x = 0.5
        else:
            if zv >= 9:
                return 1.0
            elif zv <= -9:
                return 0.0
            else:
                h = 1 / (1 + (0.2316419 * a))
                m = math.exp(-(math.pow(a, 2) / 2)) / math.sqrt(2 * math.pi)
                w = 0.31938153 * h - 0.356563782 * math.pow(h,
                                                            2) + 1.78147937 *\
                                                                 math.pow(
                    h,
                    3) - 1.821255978 * math.pow(h,
                                                4) + 1.330274429 * math.pow(
                    h, 5)
                x = (m * w)
                if (abs(mean) < abs(value)):
                    x = 1 - (m * w)
        return x

    def z_score_value(self, zvalue):
        zv = zvalue
        a = abs(zv)
        if zv == 0.0:
            x = 0.5
        else:
            if zv >= 9:
                return 1.0
            elif zv <= -9:
                return 0.0
            else:
                h = 1 / (1 + (0.2316419 * a))
                m = math.exp(-(math.pow(a, 2) / 2)) / math.sqrt(2 * math.pi)
                w = 0.31938153 * h - 0.356563782 * math.pow(h,
                                                            2) + 1.78147937 *\
                                                                 math.pow(
                    h,
                    3) - 1.821255978 * math.pow(h,
                                                4) + 1.330274429 * math.pow(
                    h, 5)
                x = 0.5 - (m * w)
        return x
