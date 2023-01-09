#!/usr/bin/python3

'''
Creation of class 'Square' to inherit
Rectangle parent class
'''
Rectangle = __import__('9-rectangle').Rectangle
''' Imported Rectangle module '''


class Square(Rectangle):
    ''' Class declared'''

    def __init__(self, size):
        ''' Constructor defined '''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        ''' Area method implemented '''
        return self.__size * self.__size

    def __str__(self):
        ''' Print function modified '''
        return ("[Rectangle] {}/{}" .format(self.__size, self.__size))
