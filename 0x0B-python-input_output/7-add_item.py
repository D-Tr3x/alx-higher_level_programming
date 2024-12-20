#!/usr/bin/python3
""" Script that adds all arguments to a Python list
    and saves them to a JSON file
"""
import sys
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """ adds all arguments to a list, then saves the list to 'filename' """

    filename = "add_item.json"
    if os.path.exists(filename):
        all_args = load_from_json_file(filename)
    else:
        all_args = []

    all_args.extend(sys.argv[1:])

    save_to_json_file(all_args, filename)


if __name__ == "__main__":
    main()
