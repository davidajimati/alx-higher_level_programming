#!/usr/bin/python3
'''
script that takes in a URL, sends a request to the URL
    and displays the value of the X-Request-Id variable
    found in the header of the response.
'''

import sys
import urllib.request

url = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(url) as res:
    r = res.info().get('X-Request-Id')
    print(r)
