#!/usr/bin/python3
"""
This function finds the peak of a  give set of numbers
"""

def find_peak(list_of_integers):
    '''
    Function declaration
    '''
    x = 0
    for i in range(list_of_integers):
        if list_of_integers[i] > x:
            x = list_of_integers[i]
    return(x)
