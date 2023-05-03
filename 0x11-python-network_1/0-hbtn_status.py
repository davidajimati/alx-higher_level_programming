#!/usr/bin/python3

'''
fetches https://alx-intranet.hbtn.io/status
    using the urllib
'''
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
r = urllib.request.Request(url)
with urllib.request.urlopen(url) as response:
    the_page = response.read()
    print(the_page)
