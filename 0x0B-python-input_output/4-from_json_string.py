#!/usr/bin/python3
'''
THis module returns an object (Python data structure)
represented by a JSON string:
'''
import json


def from_json_string(my_str):
    '''
    Returns the json object of my_obj
    '''
    return json.loads(my_str)
