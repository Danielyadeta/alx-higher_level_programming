#!/usr/bin/python3
"""
This is the "5-text_indentation" module.
The 5-text_indentation module supplies one function, text_indentation().
For example,
Hello, this is Kidus. , prints:

Hello,

 this is Kidus.

"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters:
    '.', '?' and ':'
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    line_start = 1
    for c in text:
        if line_start is 1:
            if c is ' ':
                continue
        line_start = 0
        print(c, end="")
        if c is '.' or c is '?' or c is ':':
            print("\n")
            line_start = 1
