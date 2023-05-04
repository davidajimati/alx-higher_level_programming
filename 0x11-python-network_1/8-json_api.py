#!/usr/bin/python3
'''
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
'''

import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) > 1:
        leta = argv[1]
    else:
        leta = ""
    load = {"q": leta}

    r = requests.post('http://0.0.0.0:5000/search_user', data=load)

    # check if resp is json
    try:
        resp = r.json()
        if resp != {}:
            print("[{}] {}".format(resp.get('id'), resp.get('name')))
        else:
            print("No result")
    except ValueError:
        print('Not a valid JSON')
