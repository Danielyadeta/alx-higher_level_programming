#!/usr/bin/python3
"""
This is the "0-read_file" module.
The 0-read_file module supplies one function, read_file().
"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string"""
    return json.loads(my_str)
