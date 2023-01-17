#!/usr/bin/python3

'''
Module contains a subclass that inherits fro Base
'''
from models.base import Base


class Rectangle(Base):
    ''' Class Definition '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Constructor for class '''
        super().__init__(id)
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
        self.validator(value, "width", True)
        self.__width = value

    @property
    def height(self):
        ''' gets height '''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''sets height'''
        self.validator(value, "height", True)
        self.__height = value

    @property
    def x(self):
        ''' gets x '''
        return (self.__x)

    @x.setter
    def x(self, value):
        '''sets height'''
        self.validator(value, "x", metric=False)
        self.__x = value

    @property
    def y(self):
        ''' gets y '''
        return (self.__y)

    @y.setter
    def y(self, value):
        '''sets y'''
        self.validator(value, "y", metric=False)
        self.__y = value

    def validator(self, value, name, metric):
        ''' Validates integer inputs into setters '''
        if type(value) != int:
            raise TypeError("{} must be an integer" .format(name))
        if metric and value <= 0:
            raise ValueError("{} must be > 0" .format(name))
        if not metric and value < 0:
            raise ValueError("{} must be >= 0" .format(name))
