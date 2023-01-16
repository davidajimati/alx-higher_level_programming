#!/usr/bin/python3

'''
Module contains a subclass that inherits fro Base
'''
Base = __import__('base').Base


class Rectangle(Base):
    ''' Class Definition '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Constructor for class '''
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        ''' gets width '''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''sets width'''
        self.__width = value

    @property
    def height(self):
        ''' gets height '''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''sets height'''
        self.__height = value

    @property
    def x(self):
        ''' gets x '''
        return (self.__x)

    @x.setter
    def x(self, value):
        '''sets height'''
        self.__x = value

    @property
    def y(self):
        ''' gets y '''
        return (self.__y)

    @y.setter
    def y(self, value):
        '''sets y'''
        self.__y = value
