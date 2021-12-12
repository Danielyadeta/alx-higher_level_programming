#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.

The 2-matrix_divided module supplies one function, matrix_divided().
For example,

matrix_divided([2, 4, 6], 2) returns [1, 2, 4].
"""


def matrix_divided(matrix, div):
    """ Returns the matrix division of matrix with div."""
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    mat_size = len(matrix[0])
    for i in range(len(matrix)):
        if len(matrix[i]) != mat_size:
            raise TypeError("Each row of the matrix must have the same size")
            break
    new_mat = [[0] * len(matrix[0]) for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if type(matrix[i][j]) is not int and\
                    type(matrix[i][j]) is not float:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
                break
            else:
                new_mat[i][j] = round((matrix[i][j] / div), 2)

    return new_mat
