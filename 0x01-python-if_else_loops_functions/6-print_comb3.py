#!/usr/bin/python3
for dgt1 in range(10):
    for dgt2 in range(dgt1 + 1, 10):
        if dgt1 != 8 or dgt2 != 9:
            print("{:d}{:d}".format(dgt1, dgt2), end=", ")
        else:
            print("{:d}{:d}".format(dgt1, dgt2))
