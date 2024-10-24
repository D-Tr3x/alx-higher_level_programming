#!/usr/bin/python3
"""
This module defines a function that prints a text with 2 new lines after each
of these characters: ., ? and : are found
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (string) the strings to be printed on lines

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for char in ".?:":
        text = text.replace(char, char + "\n\n")

    lines = text.split("\n")

    for line in lines:
        print(line.strip())


"""
    chars = [".", "?", ":"]
    for x in text:
        print(x, end="")

        if x in chars:
            print()
            print()

"""
