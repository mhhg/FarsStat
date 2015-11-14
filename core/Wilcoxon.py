from __future__ import division
import math

from core import Std_dev, Variance, ArithMean, ZScore


class Wilcoxon():
    def __init__(self, row1, row2):
        self.row1 = row1
        self.row2 = row2

    def differnte(self):
        difference = []
        first_paire = self.row1
        sec_paire = self.row2
        lenght = len(first_paire)
        if len(first_paire) > len(sec_paire):
            lenght = len(sec_paire)

        # calculate diffrence between two paire
        for i in range(0, lenght):
            difference.append(first_paire[i] - sec_paire[i])
        return difference

    def wilcoxon_test_indexing(self):
        difference = self.differnte()
        index = []
        temp_list = []
        sum = 0
        new_value = 0
        # sort list of difference without sign
        difference_sorted = self.arrangment(difference)
        # assign index
        for i in range(0, len(difference)):
            index.append(i + 1)
        w = {x: difference_sorted.count(x) for x in difference_sorted}
        repeat_key = [key for key, value in w.iteritems() if value > 1]
        for ind in range(0, len(difference_sorted)):
            if (ind >= new_value):
                for j in range(0, len(repeat_key)):
                    i_variable = difference_sorted[ind]
                    j_variable = repeat_key[j]
                    if i_variable == j_variable:
                        new_value = w.get(difference_sorted[ind])
                        old_index = difference_sorted.index(i_variable)
                        for k in range(0, new_value):
                            sum += old_index + (k + 1)
                        new_index = (sum / new_value)
                        for count in range(0, new_value):
                            index[(old_index + count)] = new_index
                        break
                new_value = ind + new_value
                sum = 0
        # assign sign to indexes
        rank = self.ranking(difference)
        for i in range(0, len(difference_sorted)):
            temp_list.append(difference_sorted[i])
        for i in range(0, len(rank)):
            for j in range(0, len(temp_list)):
                d_s = temp_list[j]
                n_rank = rank[i]
                if abs(n_rank) == d_s:
                    rank_index = temp_list.index(temp_list[j])
                    temp_list[rank_index] = temp_list[rank_index] * (-1)
                    index[rank_index] = index[rank_index] * (-1)
                    break
        return index

    # claculate abs of all of items in the list
    def arrangment(self, dif):
        dif_list = []
        for i in range(0, len(dif)):
            dif_list.append(abs(dif[i]))
        dif_list.sort()
        return dif_list

    def ranking(self, list):
        n_list = []
        for i in range(0, len(list)):
            if list[i] < 0:
                n_list.append(list[i])
        return n_list

    # return a list:first item of list is number of negative ranks,second is
    # mean of negative ranks and thired is sum of negative rank
    def negative_rank(self):
        indexes = self.wilcoxon_test_indexing()
        neg_rank = []
        negative_ranking = []
        for i in range(0, len(indexes)):
            if indexes[i] < 0:
                neg_rank.append(indexes[i])
        number_of_n_rank = len(neg_rank)
        mean_rank = ArithMean().mean(neg_rank)
        sum_rank = sum(neg_rank)
        negative_ranking.append(number_of_n_rank)
        negative_ranking.append(abs(mean_rank))
        negative_ranking.append(abs(sum_rank))
        return negative_ranking

    # return a list:first item of list is number of positive ranks,second is
    # mean of positive ranks and thired is sum of positive rank
    def positive_rank(self):
        indexes = self.wilcoxon_test_indexing()
        pos_rank = []
        positive_ranking = []
        for i in range(0, len(indexes)):
            if indexes[i] > 0:
                pos_rank.append(indexes[i])
        number_of_n_rank = len(pos_rank)
        mean_rank = ArithMean().mean(pos_rank)
        sum_rank = sum(pos_rank)
        positive_ranking.append(number_of_n_rank)
        positive_ranking.append(abs(mean_rank))
        positive_ranking.append(abs(sum_rank))
        return positive_ranking

    # calculate number of zero
    def ties(self):
        difference = []
        Ties = 0
        for i in range(0, len(self.row1)):
            difference.append(self.row1[i] - self.row2[i])
        for i in range(0, len(difference)):
            if difference[i] == 0:
                Ties = Ties + 1
        return Ties

    # return total number of ranks
    def total_number(self):
        lenght_list = self.row1
        lenght = []
        if len(self.row1) > len(self.row2):
            lenght_list = self.row2
        for i in range(0, len(lenght_list)):
            if lenght_list[i] != 0:
                lenght.append(lenght_list[i])

        total_number = len(lenght)
        return total_number

    # return a list with that it's lenght equals 2 and first element
    # determine test based on positive(1) or negative(0) and secend element
    # contain test statistics
    def z_value(self):
        dis_val = self.distinct_val()
        sum = 0
        sp = self.positive_rank()
        np = self.negative_rank()
        answre_list = []
        if sp[0] > np[0]:
            s = np[2]
            answre_list.append(0)
        else:
            s = sp[2]
            answre_list.append(1)
        for i in range(0, len(dis_val)):
            sum += ((dis_val[i]) ** 3) - dis_val[i]
        N = self.total_number()
        mu = (N * (N + 1)) / 4
        sigma2 = ((N * (N + 1) * (2 * N + 1)) / 24) - (sum / 48)
        sigma = math.sqrt(sigma2)
        T = (s - mu) / sigma
        answre_list.append(T)
        return answre_list

    def distinct_val(self):
        dif = self.differnte()
        sorted_dif = self.arrangment(dif)
        w = {x: sorted_dif.count(x) for x in sorted_dif}
        values = w.values()
        distinct_values = []
        for i in range(0, len(values)):
            if (values[i] > 1):
                distinct_values.append(values[i])
        return distinct_values

    # asymp.sig two taild
    def asymp_sig(self):
        dif = self.differnte()
        value_list = self.z_value()
        value = value_list[1]
        print(value)
        mean_instance = ArithMean()
        std_instance = Std_dev()
        var_instance = Variance()
        mean = mean_instance.mean(dif)
        varc = var_instance.varc(dif, mean)
        std = std_instance.Std_calc(varc)
        z_instance = ZScore()
        Asymp = 1 - (2 * z_instance.z_score_value(value))
        print(z_instance.z_score_value(value))
        return Asymp
