#!/usr/bin/python3
''' FUnction to check if a child class
    is an instance of a parent class
'''


def is_same_class(obj, a_class):
    ''' IS SAME CLASS '''
    return type(obj) is a_class
