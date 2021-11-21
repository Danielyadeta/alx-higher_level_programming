#!/usr/bin/python3


def no_c(my_string):
    lst_str = list(my_string)
    while ('c' in lst_str or 'C' in lst_str):
        if 'c' in lst_str:
            lst_str.remove('c')
        if 'C' in lst_str:
            lst_str.remove('C')

    return ("".join(lst_str))
