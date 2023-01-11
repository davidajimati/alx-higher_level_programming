#!/usr/bin/python3
import json
'''
THis module returns the JSON representation
of an object (string):
'''


def to_json_string(my_obj):
    ''' Returns the json object of my_obj'''
    new_f = json.loads(my_obj)
    return new_f
