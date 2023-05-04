#!/usr/bin/python3
'''
Interview Question - solution module
'''
import requests
from sys import argv

if __name__ == "__main__":

    owner = argv[1]
    repo = argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(repo, owner)
    r = requests.get(url)
    comt = r.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                comt[i].get("sha"),
                comt[i].get("commit").get("author").get("name")))
    except Exception:
        pass
