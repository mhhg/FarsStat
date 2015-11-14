

class Missing(object):
    No = 1
    Discrete = 2
    Range = 3

    def __init__(self, type=No, n1=0, n2=0, n3=0):
        self.type = type
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
