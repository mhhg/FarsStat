from __future__ import division
import math
from core import ZScore, ArithMean, Variance, Std_dev


class kstest():
    def __init__(self, data):
        self.data_list = data

    def f_0(self):
        data_list = self.data_list
        z_instance = ZScore()
        mean_instance = ArithMean()
        varc_instance = Variance()
        std_instance = Std_dev()
        mean = mean_instance.mean(data_list)
        varc = varc_instance.varc(data_list, mean)
        std_dev = std_instance.Std_calc(varc)
        z_list = []
        for i in range(0, len(data_list)):
            z = z_instance.z_score(mean, std_dev, data_list[i])
            z_list.insert(i, z)
        return z_list

    def f_n(self):
        val = 0.00
        data_list = self.data_list
        data_dic = {x: data_list.count(x) for x in data_list}
        value_list = data_dic.values()
        fn = []
        for i in range(0, len(value_list)):
            val += value_list[i]
            value = val / len(data_list)
            fn.insert(i, value)
        return fn

    def f_mines(self):
        data_list = self.data_list
        val = 0.00
        data_dic = {x: data_list.count(x) for x in data_list}
        value_list = data_dic.values()
        f_min = []
        for i in range(0, len(value_list)):
            val += value_list[i]
            value = (val - 1) / len(data_list)
            f_min.insert(i, value)
        return f_min

    def d_pluse(self):
        f0 = self.f_0()
        fn = self.f_n()
        dPluse = []
        for i in range(0, len(f0)):
            d = fn[i] - f0[i]
            dPluse.insert(i, d)
        dp = max(dPluse)
        return dp

    def d_mines(self):
        f0 = self.f_0()
        fmines = self.f_mines()
        d_mines = []
        for i in range(0, len(f0)):
            d = f0[i] - fmines[i]
            d_mines.insert(i, d)
        dm = max(d_mines)
        return dm

    def d_absolute(self):
        dPluse = self.d_pluse()
        dMines = self.d_mines()
        absolute = max(dPluse, dMines)
        return absolute

    def ks_z_value(self):
        D = self.d_absolute()
        data = self.data_list
        n = len(data)
        z = D * (math.sqrt(n))
        return z

    def Asymp_two_taild(self):
        z = self.ks_z_value()
        if 0 <= z and z < 0.27:
            p = 1.0
        elif 0.27 <= z and z < 1:
            q = math.exp((-1.233701) * math.pow(z, -2))
            p = 1 - (
            (2.506628 / z) * (q + (math.pow(q, 9)) + (math.pow(q, 25))))
        elif 1 <= z and z < 3.1:
            q = math.exp((-2) * (math.pow(z, 2)))
            p = 2 * (q - math.pow(q, 4) + math.pow(q, 9) - math.pow(q, 16))
        elif z <= 3.1:
            p = 0.0
        return p

    def n(self):
        return len(self.data_list)
