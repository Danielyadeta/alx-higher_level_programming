#!/usr/bin/python3
"""Definition of Rectangle class"""
import json
import models


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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = type(list_objs[0]).__name__ + ".json"
        with open(filename, "a") as f:
            delim = ", "
            f.write("[")
            for i in range(len(list_objs)):
                if i is len(list_objs) - 1:
                    delim = ""
                f.write(cls.to_json_string(
                       list_objs[i].to_dictionary()) + delim)
            f.write("]")
