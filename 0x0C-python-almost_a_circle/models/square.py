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

    @property
    def size(self):
        """ Gets the size(width/height) of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets the size (width and height) to the same value """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates attributes of Square using *args and **kwargs """
        if args:
            attr = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attr):
                    setattr(self, attr[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
