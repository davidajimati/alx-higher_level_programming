#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    from sys import stderr
    try:
        ans = fct(*args)
        return (ans)
    except (TypeError, ZeroDivisionError, IndexError):
        print("Exception: {}".format(sys.exc_info()[1]), file=stderr)
        return (None)
