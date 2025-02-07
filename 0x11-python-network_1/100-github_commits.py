#!/usr/bin/python3
""" Lists 10 commits of the repository `rails` by the user `rails`
    using `GitHub API`
"""
import sys
import requests


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)

    commits = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name"))
            )
    except IndexError:
        print(f"Error: {response.status_code}")
