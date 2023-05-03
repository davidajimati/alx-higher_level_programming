#!/usr/bin/python3
'''
script that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response.
'''

from sys import argv
import urllib.request

argv[1]
url = urllib.request.Request(argv[1])
with urllib.request.urlopen(url) as r:
