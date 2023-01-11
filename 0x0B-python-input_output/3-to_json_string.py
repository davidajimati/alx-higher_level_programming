#!/usr/bin/python3
'''
THis module returns the JSON representation
of an object (string):
'''
import json


def to_json_string(my_obj):
    '''
    Returns the json object of my_obj
    '''
    return json.dumps(my_obj)
