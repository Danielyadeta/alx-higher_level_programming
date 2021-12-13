#!/usr/bin/python3
"""
This is the "101-lazy_matrix_mul" module.
The 101-lazy_matrix_mul module supplies one function, lazy_matrix_mul().
For example,
lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]) returns:

[[ 7 10]
 [15 22]]
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices by using the module NumPy and returns result."""
    return numpy.matmul(m_a, m_b)
