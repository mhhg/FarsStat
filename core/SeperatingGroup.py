from collections import defaultdict


class SeperatingGroup():
    def __init__(self, var, group):
        self.var = var
        self.group = group

    def sepreat_group(self):
        value = self.var
        gr = self.group
        group_list = []
        for i in range(0, len(value)):
            temp = []
            temp.append(gr[i])
            temp.append(value[i])
            group_list.append(temp)
        d = defaultdict(list)
        for k, v in group_list:
            d[k].append(v)
        return d
