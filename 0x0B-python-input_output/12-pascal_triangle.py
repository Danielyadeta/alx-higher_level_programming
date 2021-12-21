#!/usr/bin/python3
"""
This is the "0-read_file" module.
The 0-read_file module supplies one function, read_file().
"""


def pascal_triangle(n):
    """Return:
        A list of lists of integers representing the
    Pascal’s triangle of n.
        An empty list if n <= 0
"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri_n = triangles[-1]
        tmp = [1]
        for i in range(len(tri_n) - 1):
            tmp.append(tri_n[i] + tri_n[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
