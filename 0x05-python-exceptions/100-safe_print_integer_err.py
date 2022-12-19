#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}" .format(value))
        return (True)

    except (ValueError, TypeError) as err:
        # print("Exception: {}" .format(err), file=sys.stderr)
        sys.stderr.write("Exception: {}\n" .format(err))
        return (False)
