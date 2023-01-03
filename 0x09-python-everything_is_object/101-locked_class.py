#!/usr/bin/python3

'''
Locked class with no object or class attribute
'''


class LockedClass:
    '''prevents the user from dynamically creating new instance
attributes, except if the new instance attribute is
called first_name.
    '''

    def __setattr__(self, attribute, value):
        if attribute == 'first_name':
            self.__dict__[attribute] = value
        else:
            raise AttributeError\
        ("'LockedClass' object has no attribute 'last_name'")
