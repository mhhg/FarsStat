# from Std_dev import Std_dev
# from Variance import *
# from var import *
from core import *
# convention (gharar dade) python ine ke esme class ha CamelCase bozor bashe
# masalan MyClass vali tabe ha snake_case base yani my_function.
class MyClass():
    # tabe constructor
    def __init__(self, data):
        self.data = data

    # tabe group
    # input: data ro az khode class migire (instance class) baad group mikone
    # input: data = [1, 2, 3, 3, 2,]
    # output: {1:1 , 2:2, 3:2}
    def group(self):
        # return
        w = {x: self.data.count(x) for x in self.data}
        return w


if __name__ == "__main__":
    my_class_instance = MyClass([16.00, 17.00, 18.00, 19.00])
    data1 = [7, -2, 2, -2, -2, -1]
    data2 = [5, 8, -8, 8, 8, 5]
    w_instance = Wilcoxon(data1, data2)
    print(w_instance.wilcoxon_test_indexing())
    print(w_instance.negative_rank())
    print(w_instance.positive_rank())
    print(w_instance.ties())
    print(w_instance.total_number())
    print(w_instance.z_value())
    print(w_instance.asymp_sig())
    print(w_instance.arrangment(data1))
