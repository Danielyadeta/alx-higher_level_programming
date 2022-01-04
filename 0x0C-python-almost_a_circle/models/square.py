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

    @property
    def size(self):
        """Gets the size of the Sqaure.

        Returns:
            The size of the Square
        """
        return self._Rectangle__width

    @size.setter
    def size(self, value):
        """Sets the size of the Square.

        Args:
            value: Value to set the size of the square
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Unofficial string representation of the Rectangle class."""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".\
            format(self.id, self._Rectangle__x, self._Rectangle__y,
                   self._Rectangle__width)

    def update(self, *args, **kwargs):
        """Update the class by assigning argument to each attribute"""
        if len(args) > 1:
            args = list(args)
            args.insert(1, args[1])
            args = tuple(args)

        if "size" in kwargs.keys():
            kwargs.update({'width': kwargs.get('size')})
            kwargs.update({'height': kwargs.get('size')})

        super().update(*args, **kwargs)

    def to_dictionary(self):
        """Returns dictionary representation of the Square."""
        dict = {}
        dict.update({'id': self.id, 'size': self._Rectangle__width,
                     'x': self._Rectangle__x,
                     'y': self._Rectangle__y})
        return dict
