#!/usr/bin/python3
""" This module provides functionality for inspecting objects
"""


def lookup(obj):
    """ Returns the list of available attributes and methods of an object
    """

    return dir(obj)
