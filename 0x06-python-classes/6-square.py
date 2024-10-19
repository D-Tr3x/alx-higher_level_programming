#!/usr/bin/python3
""" module to define class Square """


class Square:
    """ class that defines a square """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(num, int) for num in value) or \
           not all(num >= 0 for num in value):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        n = self.__size
        p = self.__position

        if n == 0:
            print()
        else:
            for _ in range(p[1]):
                print()
            for _ in range(n):
                print(" " * p[0] + "#" * n)
