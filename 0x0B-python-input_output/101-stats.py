#!/usr/bin/python3
'''
This module reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>]
"GET /projects/260 HTTP/1.1" <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
'''
import sys


def print_status():
    ''' Function to compute and print the metrics'''
    counter = 0
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    for l in sys.stdin:
        line = l.split()
        try:
            size = line[-1]
            total_size += size
            status = line[-2]
            status_codes[status] += 1
        except:
            continue

        if (counter == 9):
            print("File size: {}" .format(total_size))
            for key, value in status_codes:
                if status_codes[key] != 0:
                    print("{}: {}" .format(key, value))

        if (counter < 9):
            print("File size: {}" .format(total_size))
            for key, value in status_codes:
                if status_codes[key] != 0:
                    print("{}: {}" .format(key, value))

        counter += 1

if __name__ == "__main__":
    print_status()
