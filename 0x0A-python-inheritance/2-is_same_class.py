#!/usr/bin/python3
''' FUnction to check if a child class
    is an instance of a parent class
'''


def is_same_class(obj, a_class):
    if obj is None or a_class is None:
        return None
    ''' IS SAME CLASS '''
    return isinstance(obj, a_class)
