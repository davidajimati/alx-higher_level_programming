#!/usr/bin/python3
'''
Declaration of an empty class
'''


class BaseGeometry:
    """ Class declared and passed """

    def area(self):
        """ Computes area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates if value is an integer"""

        if type(value) is not int:
            raise TypeError("{} must be an integer" .format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0" .format(name))
