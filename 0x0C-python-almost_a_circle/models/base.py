#!/usr/bin/python3

'''
Base class module
'''
import json


class Base:
    '''Class definition '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        '''Returns a list of dictionaries in JSON'''
        if list_dictionaries is None or \
                list_dictionaries == []:
            return "[]"
        ret = json.dumps(list_dictionaries)
        return ret
