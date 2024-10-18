#!/usr/bin/pyhton3
""" Module to define class Square """


class Square:
    """ class that defines a square """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        n = self.__size

        if n == 0:
            print()
        else:
            for x in range(n):
                print("#" * n)
