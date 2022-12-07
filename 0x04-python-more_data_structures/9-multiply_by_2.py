#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    doubled = map(lambda i: i * 2, a_dictionary.values())
    return (list(doubled))
