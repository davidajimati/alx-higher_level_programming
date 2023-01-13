#!/usr/bin/python3
'''
This module contains the definition of a class `STUDENT`
and a public method that retrieves a dictionary representation
of a Student instance
'''


class Student:
    ''' Class Student '''

    def __init__(self, first_name, last_name, age):
        self.first = first_name
        self.last = last_name
        self.age = age

    def to_json(self):
        """ Public method to return the dictionary of each instance"""
        return (self.__dict__)
