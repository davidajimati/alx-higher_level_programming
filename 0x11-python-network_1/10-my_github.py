#!/usr/bin/python3
'''
This module takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
'''

from sys import argv
import requests

if __name__ == "__main__":

    username = argv[1]
    password = argv[2]

    r = requests.get('https://api.github.com/user', auth=(username, password))

    if r.status_code == 200:
        print("{}".format(r.json().get("id")))
    else:
        print("None")
