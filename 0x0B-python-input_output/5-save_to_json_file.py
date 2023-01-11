#!/usr/bin/python3
'''
THis module writes an Object to a text file,
using a JSON representation:
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Saves a python object into a text file in JSON representation
    '''
    with open(filename, 'rw') as f:
        f.write(json.dumps(my_obj))
