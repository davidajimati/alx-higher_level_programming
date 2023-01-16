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
    counter = 1
    total_size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}

    for out in sys.stdin:
        line = out.split()
        try:
            total_size += int(line[-1])
            status = str(line[-2])
            status_codes[status] += 1

        except KeyboardInterrupt:
            print("File size: {}" .format(total_size))
            for key in status_codes.keys():
                if status_codes[key] != 0:
                    print("{}: {}" .format(key, status_codes[key]))
            exit(1)

        except Exception:
            continue

        counter += 1

    print("File size: {}" .format(total_size))
    for key in status_codes.keys():
        if status_codes[key] != 0:
            print("{}: {}" .format(key, status_codes[key]))
    exit(1)


if __name__ == "__main__":
    print_status()
