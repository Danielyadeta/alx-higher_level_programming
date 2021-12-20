#!/usr/bin/python3
"""
This is the "1-my_list" module.
The 1-my_list module supplies one function, my_list(). For example,

my_list(MyList).
"""


class MyList(list):
    """a class tha inherits from list"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
