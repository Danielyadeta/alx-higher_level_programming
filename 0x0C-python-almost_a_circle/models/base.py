#!/usr/bin/python3
"""Definition of Rectangle class"""
import json
import models
import csv


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts the dictionary list to JSON string."""
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves the objects lits to file."""
        filename = cls.__name__ + ".json"
        lst = []
        if list_objs is not None:
            for i in list_objs:
                lst.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(lst))

    @staticmethod
    def from_json_string(json_string):
        """Converts the JSON string to list."""
        if json_string is not None or len(json_string) == 0:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """Creates object from dictionaries."""
        if cls.__name__ is "Rectangle":
            dummy_o = cls(9, 8)
        elif cls.__name__ is "Square":
            dummy_o = cls(98)
        dummy_o.update(**dictionary)
        return dummy_o

    @classmethod
    def load_from_file(cls):
        """Creates objects lists from a JSON string."""
        lst_r = []
        filename = cls.__name__ + ".json"
        with open(filename, "r") as f:
            lst = cls.from_json_string(f.read())
            for lsts in lst:
                lst_r.append(cls.create(**lsts))
#            lst_r = cls.create(lst)
        return lst_r

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves the object to a csv file."""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for i in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([i.id, i.width, i.height, i.x, i.y])
                if cls.__name__ == "Square":
                    writer.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """Loads the object from a csv file."""
        lst = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                i = cls.create(**dic)
                lst.append(i)
        return lst
