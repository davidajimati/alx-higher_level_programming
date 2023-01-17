#!/usr/bin/python3

'''
Module contains a subclass that inherits from Base
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
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        ''' gets height '''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''sets height'''
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        ''' gets x '''
        return (self.__x)

    @x.setter
    def x(self, value):
        '''sets height'''
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        ''' gets y '''
        return (self.__y)

    @y.setter
    def y(self, value):
        '''sets y'''
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''Method for validating the value.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        ''' Returns the area of the rectangle'''
        return (self.height * self.width)

    def display(self):
        ''' Prints the rectangle metrics with "#" symbol '''
        symbol = '#'
        xy = ('\n' * self.y + ' ' * self.x)
        print(xy, end="")

        for x in range(self.height):
            for y in range(self.width):
                print(symbol, end="")
            print()

    def __str__(self) -> str:
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal method that updates instance attributes via */**args.'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        # print(args, kwargs)
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        return {"id": self.id, "x": self.x,
                "y": self.y, "width": self.width, "height": self.height}
