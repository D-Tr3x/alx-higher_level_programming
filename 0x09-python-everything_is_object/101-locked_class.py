#!/usr/bin/python3
""" This module defines a class: LockedClass
"""


class LockedClass:
    """ A class that prevents the dynamic creation of instance attribute,
        except for 'first_name'
    """
    __slots__ = ['first_name']
