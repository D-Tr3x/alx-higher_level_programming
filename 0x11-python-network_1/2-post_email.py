#!/usr/bin/python3
""" Sends a POST request to a passed URL with email as a parameter"""
import sys
import urllib.parse
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(value).encode('ascii')
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
