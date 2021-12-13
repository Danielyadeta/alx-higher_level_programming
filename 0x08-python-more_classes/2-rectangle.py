#!/usr/bin/python3
"""Definition of Rectangle class"""


class Rectangle:
    """Defines a class rectangle.

    Attributes:
        __width: Width of the rectangle
        __height: Height of the rectangle

    Args:
        width: Width of the rectangle
        height: Height of the rectangle

    Raises:
        TypeError: If height or width is not an integer
        ValueError: If height or width is less than 0
    """
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Gets the width of the rectangle.

        Returns:
            The width the rectangle
        """
        return self.__width

    @property
    def height(self):
        """Gets the height of the rectangle.

        Returns:
            The height the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value: Value to set the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value: Value to set the height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle.

        Returns:
            The perimeter of the rectangle
        """
        return 2 * (self.__width + self.__height)
