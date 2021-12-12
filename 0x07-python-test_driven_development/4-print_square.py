#!/usr/bin/python3
"""
This is the "4-print_square" module.
The 4-print_square module supplies one function, print_square().
For example,
print_square(4) prints:

####
####
####
####
"""


def print_square(size):
    """Prints a square of size @size."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is 0:
        print()
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
