#!/usr/bin/python3
'''
Child class inherits from predefined Parent class 'list'
'''


class MyList(list):
    """ child class 'My list' """

    def print_sorted(self):
        print(sorted(list(self)))
