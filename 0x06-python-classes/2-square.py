#!/usr/bin/python3
''' Declaring a square method.
'''


class Square:
    ''' Declares class string.
    '''

    def __init__(self, size=0):
        try:
            self.__size = size
            if type(size) != int:
                raise TypeError

            if size < 0:
                raise ValueError

        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
