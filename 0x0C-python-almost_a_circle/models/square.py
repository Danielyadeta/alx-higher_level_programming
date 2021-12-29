#!/usr/bin/python3
"""Definition of Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
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
        id: id of the class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Unofficial string representation of the Rectangle class."""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".\
            format(self.id, self._Rectangle__x, self._Rectangle__y,
                   self._Rectangle__width)
