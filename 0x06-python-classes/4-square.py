#!/usr/bin/python3
'''Class to contain the methods
    Attributes of it's objects.
'''


class Square:
    ''' contain the methods
        Attributes of it's ojects
    '''

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        a = self.__size * self.__size
        return a
