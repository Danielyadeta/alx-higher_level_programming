#!/usr/bin/python3
"""
This is the "0-lookup" module.
The 0-lookup module supplies one function, lookup(). For example,

lookup(MyClass1)
"""


def lookup(obj):
    """returns the list of available attributes and methods of an object"""
    return dir(obj)
