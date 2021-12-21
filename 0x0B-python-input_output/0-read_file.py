#!/usr/bin/python3
"""
This is the "0-read_file" module.
The 0-read_file module supplies one function, read_file().
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout."""
    with open(filename) as f:
        read_data = f.read()

    print(read_data, end="")
