#!/usr/bin/python3
'''
This module builds on the module on 10-student.py
And a Public method def reload_from_json(self, json):
that replaces all attributes of the Student instance:
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

    def reload_from_json(self, json):
        try:
            ''' Replaces the students details '''
            self.first_name = json["first_name"]
            self.last_name = json["last_name"]
            self.age = json["age"]
        except Exception:
            pass
