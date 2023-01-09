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
        """Method for validate if a num is integer"""

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
