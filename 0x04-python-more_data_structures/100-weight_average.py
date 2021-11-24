#!/usr/bin/python3


def weight_average(my_list=[]):
    item_0 = [item[0] for item in my_list]
    item_1 = [item[1] for item in my_list]
    sum_n_0 = 0
    sum_n_1 = 0

    for i in range(len(item_0)):
        sum_n_0 = sum_n_0 + (item_0[i] * item_1[i])

    for i in item_1:
        sum_n_1 = sum_n_1 + i

    return sum_n_0 / sum_n_1
