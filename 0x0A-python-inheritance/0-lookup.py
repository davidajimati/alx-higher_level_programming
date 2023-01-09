#!/usr/bin/python3

'''
Function to return the list of special attributes applicable to an object
'''


def lookup(obj):
    '''
    Accepts an object and checks the type.
    If not None, then returns the dir(ob)
    '''
    if obj is None:
        return (None)
    return (dir(obj))

