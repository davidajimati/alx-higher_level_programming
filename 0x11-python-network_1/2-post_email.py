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

    email = argv[2]
    url = argv[1]

    # encode email
    value = urllib.parse.urlencode(url)
    value = value.encode

    full_url = url + '?' + value
    request = urllib.request.Request(url, value)
    with urllib.request.urlopen(request) as response:
        body = response.read()
        parsed_body = urllib.parse.urlparse(body)
        print(body.decode('utf-8'))
