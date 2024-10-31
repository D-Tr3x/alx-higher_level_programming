#!/usr/bin/python3
""" Module defines a student with first_name, last_name and age attributes """


class Student:
    """ Represents a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
