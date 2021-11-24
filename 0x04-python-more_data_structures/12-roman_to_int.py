#!/bin/usr/python3


def roman_to_int(roman_string):
    a_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
    keys = list(a_dictionary.keys())
    num = 0
    for i in roman_string:
        if i not in keys:
            return None
        num = num + a_dictionary.get(i)

    return num
