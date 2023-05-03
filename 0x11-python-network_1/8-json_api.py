#!/usr/bin/python3
'''
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
'''

import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    r = requests.post('http://0.0.0.0:5000/search_user', params=q)
    resp = r.json()

    # check if resp is json
    if type(resp) == dict:

        if len(resp) != 0:
            for k, v in resp.items():
                print("{} {}".format(k, v))
        else:
            print("No result")
    else:
        print('Not a valid JSON')
