#!/usr/bin/python3
""" Sends a POST request to http://0.0.0.0:5000/search_user
    with a letter as a parameter
"""
import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]

    value = {"q": letter}

    r = requests.post('http://0.0.0.0:5000/search_user', data=value)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    except ValueError:
        print("Not a valid JSON")
