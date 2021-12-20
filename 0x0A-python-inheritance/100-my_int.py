#!/usr/bin/python3
"""
Module containing MyInt class.
"""


class MyInt(int):
    """MyInt is a rebel. MyInt has == and != operators inverted"""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """override of the equals attribute"""
        return int(self) != other

    def __ne__(self, other):
        """override of the not equals attribute"""
        return int(self) == other
