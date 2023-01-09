#!/usr/bin/python3
'''
Child class inherits from predefined Parent class 'list'
'''


class MyList(list):
    """ child class 'My list' """
    pass

    def print_sorted(self):
        """ function to print sorted list"""
        print(sorted(list(self)))
