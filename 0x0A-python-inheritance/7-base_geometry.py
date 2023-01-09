#!/usr/bin/python3
'''
Declaration of an empty class
'''


class BaseGeometry:
    """ Class declared and passed """

    def integer_validator(self, name, value):
        """ validates if value is an integer"""

        self.name = name
        self.value = value
        if type(self.value) is not int:
            raise TypeError("{} must be an integer" .format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0" .format(self.name))

    def area(self):
        """ Computes area """
        raise Exception("area() is not implemented")
