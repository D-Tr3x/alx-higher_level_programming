#!/usr/bin/python3
def multiple_returns(sentence):
    len = 0
    for char in sentence:
        len += 1
    length = 0
    first = ""
    if sentence == "":
        length = 0
        first +=  None
    else:
        length = len
        first += sentence[0]

    return (length, first)
