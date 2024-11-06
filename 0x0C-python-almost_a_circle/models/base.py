#!/usr/bin/python3
""" Module: defines base Class with `id` attribute """

import json


class Base:
    """ Base class for classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes id(int) to Base

        Assigns id automatically if None,
        otherwise; assigns id to number of instances
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        file = f"{cls.__name__}.json"

        if list_objs is None:
            data = []
        else:
            data = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(data)
        with open(file, 'w') as f:
            json.dump(data, f)
            # f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """

        if not json_string:
            return []
        return json.loads(json_string)
