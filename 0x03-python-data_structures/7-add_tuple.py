#!/usr/bin/python3
# this program adds the first 2 integers of two tuples
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0 and len(tuple_b) == 0:
        return None

    l1 = list(tuple_a)
    l2 = list(tuple_b)
    # lf = [0, 0]

    # l1 += [0, 0]
    # l2 += [0, 0]

    # lf[0] = l1[0] + l2[0]
    # lf[1] = l1[1] + l2[1]

    return tuple(l1[0] + l2[0], l1[1] + l2[1])
