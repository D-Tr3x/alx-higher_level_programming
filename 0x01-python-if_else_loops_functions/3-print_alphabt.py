#!/usr/bin/python3
for alpha in range(ord('a'), ord('z') +1):
    if alpha == ord('q') or alpha == ord('e'):
        print("", end="")
    else:
        print("{}".format(chr(alpha)), end="")
