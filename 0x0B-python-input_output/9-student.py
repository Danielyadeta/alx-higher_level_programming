#!/usr/bin/python3
"""
This is the "0-read_file" module.
The 0-read_file module supplies one function, read_file().
"""


class Student:
    """Definition of the class Student.

    Attributes:
        first_name: The first name
        last_name: The last name
        age: the age

    Args:
        first_name: First name argument
        last_name: Last name argument
        age: Age argument
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance."""
        return self.__dict__
