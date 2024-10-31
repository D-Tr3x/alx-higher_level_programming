#!/usr/bin/python3
""" Module: defines a function that creates object from a JSON file """
import json


def load_from_json_file(filename):
    """ Creates an Object from a “JSON file”: filename """

    with open(filename, mode="r", encoding="utf-8") as file:
        return json.load(file)
