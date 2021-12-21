#!/usr/bin/python3
"""
This is the "0-read_file" module.
The 0-read_file module supplies one function, read_file().
"""
import json


def load_from_json_file(filename):
    """a function that creates an Object from a JSON file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
