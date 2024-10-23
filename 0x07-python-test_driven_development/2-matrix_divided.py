#!/usr/bin/python3
"""
This module defines a function which divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor

    Args:
        matrix (list of lists): containing integers or floats
        div (int or float): The divisor

    Returns:
        list of lists: the divided matrix

    Raises:
        TypeError: if matrix is not a list of lists of integers or floats
        TypeError: if rows of the matrix are not the same size
        ZeroDivisionError: if div is zero
    """
    new_matrix = []
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
