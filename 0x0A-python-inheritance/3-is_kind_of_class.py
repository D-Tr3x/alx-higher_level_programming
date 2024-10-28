#!/usr/bin/python3
""" This module defines a function that determines if an object is an instance
    of a class or a superclass
"""


def is_kind_of_class(obj, a_class):
    """ Returns True if the obj is an instance of a_class or its superclass;
        otherwise returns False
    """
    return isinstance(obj, a_class)
