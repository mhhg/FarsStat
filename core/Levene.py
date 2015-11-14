from core import SeperatingGroup

class Levene():
    def __init__(self, value, group):
        self.value = value
        self.group = group

    def leven_test(self):
        val = self.value
        gr = self.group
        sep_ins = SeperatingGroup(val, gr)
        d = sep_ins.sepreat_group()
        value_list = d.values()










