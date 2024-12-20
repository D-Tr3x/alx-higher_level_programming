#!/usr/bin/python3
""" Defines a Rectangle class that inherits from Base """

from models.base import Base


class Rectangle(Base):
    """ Represents a rectangle; with `width`, `height`, `x` and `y` attributes
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize attributes: width, height, x, y and id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """ Returns the area value of the Rectangle instance """
        return self.__width * self.__height

    def display(self):
        """ Prints the rectangle with the `#` character, handling `x` and `y`
        """

        print("\n" * self.__y, end="")
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """ Updates attributes of Rectangle using *args and **kwargs
        """
        if args:
            attr = ['id', 'width', 'height', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attr):
                    setattr(self, attr[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def __str__(self):
        """ Returns a formatted string representation of the rectangle """
        return (f"[Rectangle] ({self.id}) "
                f"{self.__x}/{self.__y} - {self.__width}/{self.__height}")

    def to_dictionary(self):
        """ Returns the dictionary representation of the Rectangle,
            containing: id, width, height, x and y
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
