#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    kiy = None
    biggest = 0

    for key, value in a_dictionary.items():
        if value > biggest:
            biggest = value
            kiy = key

    return kiy
