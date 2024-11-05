#!/usr/bin/python3
""" Module: defines base Class with `id` attribute """


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
