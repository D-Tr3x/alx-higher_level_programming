#!/usr/bin/python3
""" This module defines MyInt class that inherits from int
"""


class MyInt(int):
    """ A rebel integer class with inverted == and != operators
    """

    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
