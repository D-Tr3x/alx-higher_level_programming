#!/usr/bin/python3
""" Module to define class Square """


class Square:
    """ class that defines a Square """
    def __init__(self, size=0):
        self.__size = size

        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def get_size(self):
        return self.__size

    def area(self):
        return self.__size ** 2
