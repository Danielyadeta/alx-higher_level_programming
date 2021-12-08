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
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if len(position) < 2 or type(position[0]) is not int or\
                type(position[1]) is not int or\
                position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """Calculates the area of the square.

        Returns:
            The area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Gets the size of the square.

        Returns:
            The size the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size.

        Args:
            value: Value to set size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Gets the position tuple.

        Returns:
            The position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position.

        Args:
            value: position value to set
        """
        if len(value) < 2 or type(value[0]) is not int or\
                type(value[1]) is not int or\
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def my_print(self):
        """Prints the square"""
        if self.__size is 0:
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    def __str__(self):
        """Prints the square"""
        if self.__size is 0:
            return ""
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            if i is not self.__size - 1:
                print()
        return ""
