#!/usr/bin/python3
'''
Pyhton OOP - more classes - Task 1
'''


class Rectangle:
    '''
    This class contains the definition of the class 'Rectangle'
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("eight must be >= 0")
        self.__height = value

    def area(self):
        return (self.height * self.width)

    def perimeter(self):
        return (2 * (self.height * self.width))

    def __str__(self):
        for i in range(self.height):
            for j in range(self.width):
                print("#", end="")
            print('')
        return ('')


# my_rectangle = Rectangle(2, 4)
# print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

# print(str(my_rectangle))
# print(repr(my_rectangle))

# print("--")

# my_rectangle.width = 10
# my_rectangle.height = 3
# print(my_rectangle)
# print(repr(my_rectangle))
