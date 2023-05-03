#!/usr/bin/python3
'''
Takes in a URL and an email, sends a POST request to
    the passed URL with the email as a parameter, and
    displays the body of the response (decoded in utf-8)
'''

if __name__ == "__main__":

    from sys import argv
    import urllib.parse
    import urllib.request

    url = argv[1]
    val = {'email': argv[2]}

    # encode val
    value = urllib.parse.urlencode(val).encode('ascii')
    req = urllib.request.Request(url, data=value)

    with urllib.request.urlopen(req) as response:
        parsed_body = urllib.parse.urlparse(response.read()).decode('utf-8')
        print(parsed_body)
