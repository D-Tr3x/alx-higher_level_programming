#!/usr/bin/python3
"""
Module that provides a function: add_integer, to add two numbers after
converting floats to integers
"""


def add_integer(a, b=98):
    """
    Adds two numbers after casting floats to integers.

    Args:
         a (int or float): the first number
         b (int or float): the second number, defaults to 98

    Returns:
         the sum of a and b

    Raises:
         TypeError: if a or b is not an integer or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    if isinstance(a, float) and (a != a):
        raise ValueError('a must be an integer')
    if isinstance(b, float) and (b != b):
        raise ValueError('b must be an integer')

    return int(a) + int(b)
