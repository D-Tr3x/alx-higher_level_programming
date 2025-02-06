#!/usr/bin/python3
""" Defines a function that finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """Returns the peak of a list of integers"""

    if not list_of_integers:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    half = int(size / 2)
    peak = list_of_integers[half]  # assume the peak is at the center

    if peak > list_of_integers[half - 1] and peak > list_of_integers[half + 1]:
        return peak  # since it is greater than its neighbours
    elif peak < list_of_integers[half - 1]:
        # recursively search from the beginning to the middle
        return find_peak(list_of_integers[:half])
    else:
        # recursively search one past the middle till the end
        return find_peak(list_of_integers[half + 1:])
