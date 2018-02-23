import numpy as np
import logging

logging.basicConfig(filename='logging.txt', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y &I:%M:%S %p', level=logging.DEBUG)


class NumbersFunction:

    def __init__(self, num_list=None):
        self.num_list = num_list

    def sum_list(self):
        print("The sum is ", np.sum(self.num_list))
        return np.sum(self.num_list)

    def find_min_max(self):
        print("The minimum is ", np.min(self.num_list))
        print("The maximum is ", np.max(self.num_list))
        return np.min(self.num_list) & np.max(self.num_list)

    def max_diff(self):
        print("The maximum difference is ", np.max(self.num_list)-np.min(self.num_list))
        return np.max(self.num_list)-np.min(self.num_list)


x = NumbersFunction([1, 2, 3, 4])
x.sum_list()
x.find_min_max()
x.max_diff()
