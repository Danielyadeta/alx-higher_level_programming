#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(). For example,

add_integer(1, 2) returns 3.
"""


def add_integer(a, b=98):
    """ Returns the addition of a and b, an exact integer."""
    if type(a) is not int and\
            type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and\
            type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
