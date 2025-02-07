#!/usr/bin/python3
""" Sends a request to a URL and displays the body of the response,
    handling the HTTP Errors
"""
import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]

    response = requests.get(url)

    if int(response.status_code) >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
