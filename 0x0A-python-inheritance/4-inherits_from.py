#!/usr/bin/python3
""" This module defines a function which determines if an object is an instance
    of a sub-class but not the class
"""


def inherits_from(obj, a_class):
    """ Returns True if the obj is an instance of a class that inherited
    (directly or indirectly) from the a_class; else returns False
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
