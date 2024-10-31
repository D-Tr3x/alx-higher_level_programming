#!/usr/bin/python3
""" Module: Class to JSON
"""


def class_to_json(obj):
    """ Returns a dictionary description for JSON serialization of an object
    """
    json_dict = {}

    for attr in dir(obj):
        if attr.startswith('__') and attr.endswith('__'):
            continue

        value = getattr(obj, attr)
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value

    return json_dict
