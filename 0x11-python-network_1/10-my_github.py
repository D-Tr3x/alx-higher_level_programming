#!/usr/bin/python3
""" Takes my GitHub credentials (username and password) as arguments
    and uses the `GitHub Api` to display my `id`
"""
import sys
import requests


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get('https://api.github.com/user', auth=(username, password))
    print(r.json().get("id"))
