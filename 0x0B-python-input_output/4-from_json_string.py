#!/usr/bin/python3
""" Module: defines a function that converts Python data to JSON
"""


import json


def from_json_string(my_str):
    """ Returns an object (Python data structure) represented by a JSON string
    """

    py_string = json.loads(my_str)
    return py_string
