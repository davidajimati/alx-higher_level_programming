#!/usr/bin/python3
"""
This function finds the peak of a  give set of numbers
"""


def find_peak(list_of_integers):
    '''
    Function declaration
    '''
    x = 0
    for i in list_of_integers:
        if i > x:
            x = i
    return (x)
