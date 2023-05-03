#!/usr/bin/python3
'''
takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8).
'''

from sys import argv
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as response:
            print(response.read())
    except urllib.error.HTTPError as e:
        print(e.code)
