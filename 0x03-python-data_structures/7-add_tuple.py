#!/usr/bin/python3
# this program adds the first 2 integers of two tuples
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        return None
    # covert the tuple to lists
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    list_f = []

    # iterate through the lists
    list_f[0] = list_a[0] + list_b[0]
    list_f[1] = list_a[1] + list_b[1]

    return tuple(list_f)
