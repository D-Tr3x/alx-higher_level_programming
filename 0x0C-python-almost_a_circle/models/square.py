#!/usr/bin/python3
""" Defines a class Square that inherits from Rectangle """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Represents a square that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes attributes to Square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns the string representation of Square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
