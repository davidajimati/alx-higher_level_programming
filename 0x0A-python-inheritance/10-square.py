#!/usr/bin/python3

'''
Creation of class 'Square' to inherit
Rectangle parent class
'''
Rectangle = __import__('9-rectangle').Rectangle
''' Imported Rectangle module '''


class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return ("[Rectangle] {}/{}" .format(self.__size, self.__size))
