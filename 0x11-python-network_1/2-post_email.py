#!/usr/bin/python3
'''
Takes in a URL and an email, sends a POST request to
    the passed URL with the email as a parameter, and
    displays the body of the response (decoded in utf-8)
'''

if __name__ == "__main__":

    from sys import argv
    import urllib.request

    email = argv[1]
    url = argv[2]

    full_url = urllib.request.Request(url, email)
    with urllib.request.urlopen(full_url) as response:
        body = response.read()
        print(body.decode('utf-8'))
