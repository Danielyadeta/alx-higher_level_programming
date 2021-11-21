#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    lst = []

    for i in my_list:
        lst.append(i % 2 == 0)

    return (lst)
