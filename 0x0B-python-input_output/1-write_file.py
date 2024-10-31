#!/usr/bin/python3
""" Module: Function that writes to a file then reads """


def write_file(filename="", text=""):
    """ Writes a string to a text file (UTF8)
        and returns the number of characters written
    """

    with open(filename, mode="w", encoding="utf-8") as file:
        written = file.write(text)
        return written
