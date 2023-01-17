#!/usr/bin/python3

'''
Module contains a subclass that inherits fro Base
'''
Base = __import__('base').Base


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
        self.validator("width", value, metric=True)

    @property
    def height(self):
        ''' gets height '''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''sets height'''
        self.validator("height", value, metric=True)
        self.__height = value

    @property
    def x(self):
        ''' gets x '''
        return (self.__x)

    @x.setter
    def x(self, value):
        '''sets height'''
        self.validator("x", value, metric=False)
        self.__x = value

    @property
    def y(self):
        ''' gets y '''
        return (self.__y)

    @y.setter
    def y(self, value):
        '''sets y'''
        self.validator("y", value, metric=False)
        self.__y = value

    def validator(self, name, value, metric):
        ''' Validates integer inputs into setters '''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer" .format(name))
        if metric and value <= 0:
            raise ValueError("{} must be > 0" .format(name))
        if not metric and value < 0:
            raise ValueError("{} must be >= 0" .format(name))
