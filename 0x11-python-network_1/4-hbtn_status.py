#!/usr/bin/python3
""" Fetches https://alx-intranet.hbtn.io/status using `requests` package """
import requests


if __name__ == '__main__':
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
