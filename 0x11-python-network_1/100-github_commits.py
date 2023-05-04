#!/usr/bin/python3

'''
Interview Question - solution module
'''

import requests
from sys import argv
if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(repo, owner)
    r = requests.get(url)

    if r.status_code == 200:
        commits = r.json()

        i = 0
        while i < 10:
            print("{}: {}" .format(commits[i].get('sha'), commits[i].get(
                'commit').get('author').get('name')))
            i += 1
