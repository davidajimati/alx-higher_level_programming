#!/usr/bin/python3

'''
if the object is an instance of a class that inherited (directly or indirectly)
 from the specified class
'''


def inherits_from(obj, a_class):
    """ function declaration """
    return issubclass(obj, a_class)
