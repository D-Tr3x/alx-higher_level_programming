#!/usr/bin/pyhton3
"""
This module creates a function that prints a users fullname
"""

def say_my_name(first_name, last_name=""):
    """
    prints My name is <first name> <last name>

    Args:
        first_name (string)
        last_name (string, optional)
    Raises:
        TypeError if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
