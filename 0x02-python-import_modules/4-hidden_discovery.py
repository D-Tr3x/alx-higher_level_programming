#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    names = dir(hidden_4)
    for all in sorted(names):
        if not all.startswith("__"):
            print(all)
