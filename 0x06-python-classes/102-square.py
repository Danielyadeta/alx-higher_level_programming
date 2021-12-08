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

    def __eq__(self, other_square):
        """Defines the == comparision."""
        return self.area() == other_square.area()

    def __ne__(self, other_square):
        """Defines the != comparison."""
        return self.area() != other_square.area()

    def __lt__(self, other_square):
        """Defines the < comparison."""
        return self.area() < other_square.area()

    def __gt__(self, other_square):
        """Defines the > comparison."""
        return self.area() > other_square.area()

    def __le__(self, other_square):
        """Defines the <= comparison."""
        return self.area() <= other_square.area()

    def __ge__(self, other_square):
        """Defines the >= compmarison."""
        return self.area() >= other_square.area()
