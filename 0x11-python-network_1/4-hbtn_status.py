#!/usr/bin/python3
'''
This module fetches https://alx-intranet.hbtn.io/status
    uses the package requests
    No package imports other than requests
'''

import requests
if __name__ == "__main__":

    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
