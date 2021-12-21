#!/usr/bin/python3
"""
This is the "0-read_file" module.
The 0-read_file module supplies one function, read_file().
"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and returns the
        number of characters written.
    """
    with open(filename, "w") as f:
        write_bytes = f.write(text)

    return write_bytes
