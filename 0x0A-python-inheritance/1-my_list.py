#!/usr/bin/python3
""" Module for MyList class that inherits from list
"""


class MyList(list):
    """ Subclass of list, with a method that prints the list in an order
    """

    def print_sorted(self):
        """ prints the list in an ascending order
        """
        print(sorted(self))
