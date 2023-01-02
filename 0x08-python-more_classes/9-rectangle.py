#!/usr/bin/python3
"""
This is the "Rectangle"  module.
This module provides a simple Rectangle class.
"""


class Rectangle:
    """A Rectangle class with attributes width and height, and
    methods area, perimeter, print, and str.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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
        return (2 * (self.height + self.width))

    def __str__(self):
        if not self.width or not self.height:
            print("Bye rectangle...")
        rect = ""
        if self.width == 0 and self.height == 0:
            return rect

        for i in range(self.height):
            rect += (str(self.print_symbol) * self.width)
            if i is not self.height - 1:
                rect += '\n'
        return (rect)

    def __repr__(self):
        return ('Rectangle({}, {})' .format(self.width, self.height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        cls.width = size
        cls.height = size




my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)