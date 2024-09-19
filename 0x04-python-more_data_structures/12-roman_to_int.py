#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev = 0

    for numerals in reversed(roman_string):
        if numerals not in roman:
            return 0
        num = roman[numerals]
        if num < prev:
            result -= num
        else:
            result += num
        prev = num

    return result
