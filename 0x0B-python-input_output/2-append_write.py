#!/usr/bin/python3
"""
This is the "0-read_file" module.
The 0-read_file module supplies one function, read_file().
"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8) and
        returns the number of characters added.
    """
    with open(filename, "a") as f:
        write_bytes = f.write(text)

    return write_bytes
