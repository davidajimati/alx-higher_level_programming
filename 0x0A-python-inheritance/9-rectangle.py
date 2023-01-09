#!/usr/bin/python3

'''
Creation of class 'Rectangle' to inherit
Basegeometry parent class
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry
''' Rectangle module '''


class Rectangle(BaseGeometry):
    ''' inherit's BaseGeometry'''

    def __init__(self, width, height):
        """ Private attributes declared"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}" .format(self.__width, self.__height))
