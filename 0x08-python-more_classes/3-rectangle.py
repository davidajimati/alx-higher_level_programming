#!/usr/bin/python3
"""
This is the "Rectangle"  module.
This module provides a simple Rectangle class.
"""


class Rectangle:
    """A Rectangle class with attributes width and height, and
    methods area, perimeter, print, and str.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        return (2 * (self.height * self.width))

    def __str__(self):
        rect = ""
        # if self.width == 0 and self.height == 0:
        #     return rect

        for i in range(self.height):
            rect += ("#" * self.width)
            if i is not self.height - 1:
                rect += '\n'
        return (rect)
