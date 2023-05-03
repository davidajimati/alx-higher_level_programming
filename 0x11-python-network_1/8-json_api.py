#!/usr/bin/python3
'''
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
'''

import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) > 1:
        lit = argv[1]
    else:
        lit = ""

    load = {'q': lit}

    r = requests.post('http://0.0.0.0:5000/search_user', params=load)

    # check if resp is json
    try:
        resp = r.json()
        if resp != {}:
            for k, v in resp.items():
                print("{} {}".format(k, v))
        else:
            print("No result")
    except Exception:
        print('Not a valid JSON')
