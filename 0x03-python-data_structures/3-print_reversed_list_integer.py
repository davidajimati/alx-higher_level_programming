#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    tot = len(my_list) - 1
    while tot >= 0:
        tot -= 1
        print("{:d}" .format(my_list[tot]))
