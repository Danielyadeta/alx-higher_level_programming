#!/usr/bin/python3
"""Definition of Square class"""


class Square:
    """Defines a class square.

    Attributes:
        __size: Size of the square

    Args:
        __size: Size of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    def __int__(self, size = 0):
        if size < 0:
            raise ValueError("size must be >= 0")
        elif type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            self.__size = size
