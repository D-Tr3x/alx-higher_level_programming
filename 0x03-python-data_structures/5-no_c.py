#!/usr/bin/python3
def no_c(my_string):
    copy_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            copy_string += char

    return copy_string
