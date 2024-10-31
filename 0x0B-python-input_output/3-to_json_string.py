#!/usr/bin/python3
""" Module: defines a function that converts a python object to JSON repr...
"""

import json


def to_json_string(my_obj):
    """ Returns the JSON representation of my_obj(string) """

    j_string = json.dumps(my_obj)
    return j_string
