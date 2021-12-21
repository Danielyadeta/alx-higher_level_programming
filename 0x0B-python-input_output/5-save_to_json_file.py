#!/usr/bin/python3
"""
This is the "0-read_file" module.
The 0-read_file module supplies one function, read_file().
"""
import json


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file,
    using a JSON representation.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
