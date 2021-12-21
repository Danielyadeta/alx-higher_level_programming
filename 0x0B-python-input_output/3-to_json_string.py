#!/usr/bin/python3
"""
This is the "0-read_file" module.
The 0-read_file module supplies one function, read_file().
"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
