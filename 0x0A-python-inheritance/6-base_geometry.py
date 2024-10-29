#!/usr/bin//python3
""" This module provides geometry classes.
"""


class BaseGeometry:
    """ Base class for geometric shapes. """

    def area(self):
        raise Exception('area() is not implemented')
