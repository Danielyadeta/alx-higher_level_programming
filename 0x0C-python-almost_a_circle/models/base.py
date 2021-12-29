#!/usr/bin/python3
"""Definition of Rectangle class"""


class Base:
    """Defines a class rectangle.

    Attributes:
        __nb_objects: Width of the rectangle
        id: id of the class

    Args:
        id: id of the class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1;
            self.id = Base.__nb_objects
