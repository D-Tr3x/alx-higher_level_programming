#!/usr/bin/python3
"""
This module defines a function that prints a square with '#' characters
"""


def print_square(size):
    """
    Prints a square with the character #

    Args:
        size (int or float): the length of the square

    Raise:
        TypeError: if size is not an integer
                   if size is a float and less than zero
        ValueError: if size is less than zero
    """
    if not isinstance(size, (int, float)):
        raise TypeError('size must be an integer')
    if isinstance(size, float) and size < 0:
        raise TypeError('size must be an integer')
    elif isinstance(size, int) and size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
