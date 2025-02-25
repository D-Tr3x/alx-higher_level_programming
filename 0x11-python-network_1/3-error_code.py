#!/usr/bin/python3
""" Sends a request to a URL and display the body of the response,
    handling HTTP Errors
"""
import sys
import urllib.error
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
