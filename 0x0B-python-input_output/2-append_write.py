#!/usr/bin/python3
""" Module: defines a function that appends a text to a file when called """


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8),
        returns the number of characters added
    """

    with open(filename, mode="a", encoding="utf-8") as file:
        appended = file.write(text)
        return appended
