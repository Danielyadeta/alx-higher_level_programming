#!/usr/bin/python3
"""Module containing the function add_attribute."""


def add_attribute(obj, att, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object to add attribute to.
        att: The name of the attribute to add.
        value: The value of the attribute

    Raises:
        TypeError: If the attribute can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
