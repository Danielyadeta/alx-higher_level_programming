#!/usr/bin/python3
"""
This is the "0-read_file" module.
The 0-read_file module supplies one function, read_file().
"""


def append_after(filename="", search_string="", new_string=""):
    """a function that inserts a line of text to a file,
    after each line containing a specific string.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        list_line = []
        while True:
            line = f.readline()
            if line == "":
                break
            list_line.append(line)
            if search_string in line:
                list_line.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(list_line)
