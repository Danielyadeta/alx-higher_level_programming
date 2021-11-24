#!/usr/bin/python3


def uniq_add(my_list=[]):
    uniq_lst = set(my_list)
    sum = 0
    for i in uniq_lst:
        sum = sum + i

    return sum
