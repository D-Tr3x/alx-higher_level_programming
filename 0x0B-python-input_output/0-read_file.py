#!/usr/bin/python3
""" Module: file reader, with function: read_file """


def read_file(filename=""):
    """ Reads a text file (UTF8) and prints it to stdout """

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
