#!/usr/bin/python3


def best_score(a_dictionary):
    max_key = None
    if a_dictionary is not None:
        keys = list(a_dictionary.keys())
        max_num = a_dictionary.get(keys[0])
        for i in keys:
            if a_dictionary.get(i) > max_num:
                max_num = a_dictionary.get(i)
                max_key = i

    return max_key
