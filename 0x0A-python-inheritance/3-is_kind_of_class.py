#!/usr/bin/python3
"""
Module Containing the function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """returns True if object is an instance or inherited from a_class, else False"""
    return (isinstance(obj, a_class))
