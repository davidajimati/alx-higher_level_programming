#!/usr/bin/python3

'''
Locked class with no object or class attribute
'''

class LockedClass:
    '''
    prevents the user from dynamically creating new instance 
    attributes, except if the new instance attribute is 
    called first_name.
    '''
    pass
