#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    doubled = {}
    for key, value in a_dictionary.items():
        doubled[key] = value * 2
    return (doubled)
