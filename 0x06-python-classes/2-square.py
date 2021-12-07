#!/usr/bin/python3
"""Definition of Square class"""


class Square:
    """Defines a class square.

    Attributes:
        __size: Size of the square

    Args:
        size: Size of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
