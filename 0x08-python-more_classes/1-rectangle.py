#!/usr/bin/python3
'''
Pyhton OOP - more classes - Task 1
'''


class Rectangle:
    '''
    This class contains the definition of the class 'Rectangle'
    '''

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__eight = height

    def width(self):
        return (self.width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def height(self):
        return (self.height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("eight must be >= 0")
        self.__height = value
