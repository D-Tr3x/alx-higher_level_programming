#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]
    argc = len(argv)

    if argc < 1:
        print(f"{argc} arguments.")
    elif argc == 1:
        print(f"{argc} argument:")
        print(f"{argc}: {argv[0]}")
    else:
        print(f"{argc} arguments:")
        for i in range(argc):
            print(f"{i + 1}: {argv[i]}")
