#!/usr/bin/python3
'''
This module builds on the module on 9-student.py
returns only the key pairs if attrs is a list of strings
else returns all the dictionary values
'''


class Student:
    ''' Class Student '''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Public method to return the dictionary of each instance"""
        if attrs is None:
            return (self.__dict__)
        else:
            ret_dict = {}
            for i in attrs:
                if i not in self.__dict__:
                    continue
                else:
                    ret_dict[i] = self.__dict__[i]
            return ret_dict
