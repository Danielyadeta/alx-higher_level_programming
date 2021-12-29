#!/usr/bin/python3
"""Definition of Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defines a class rectangle.

    Attributes:
        __width: Width of the rectangle
        __height: Height of the rectangle
        __x: x dimen
        __y: y dimen

    Args:
        width: Width of the rectangle
        height: Height of the rectangle
        x: x dimen
        y: y dimen
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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

    @property
    def x(self):
        """Gets the x value of the rectangle.
        Returns:
            The x value the rectangle
        """
        return self.__x

    @property
    def y(self):
        """Gets the y value of the rectangle.

        Returns:
            The y value the rectangle
        """
        return self.__y

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value: Value to set the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value: Value to set the height of the rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x value of the rectangle.
        Args:
            value: Value to set the x of the rectangle
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y value of the rectangle.
        Args:
            value: Value to set the y of the rectangle
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
