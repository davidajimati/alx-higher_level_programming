#!/usr/bin/python3

'''
fetches https://alx-intranet.hbtn.io/status
    using the urllib
'''
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
r = urllib.request.Request(url)
with urllib.request.urlopen(url) as response:
    r = response.read()

    print("Body response:")
    print("\t- type: {}$".format(type(r)))
    print("\t- content: {}$".format(r))
    print("\t- utf8 content: {}$".format(r.decode('utf-8')))
