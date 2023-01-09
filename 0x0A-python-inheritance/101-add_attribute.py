#!/usr/bin/python3

'''
*function that adds a new attribute to an object if it’s possible
*Raise a TypeError exception, with the message
can't add new attribute if the object can’t have new attribute
*You are not allowed to use try/except
*You are not allowed to import any module
'''


def add_attribute(object, item, value):
    ''' Function declaration '''
    if object:
        setattr(object, item, value)
        return
    raise TypeError("can't add new attribute")
