#!/usr/bin/python3
'''
This module writes an Object to a text file,
using a JSON representation:
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Saves a python object into a text file in JSON representation
    '''
    with open(filename, 'w') as file:
        file.write(json.dumps(my_obj))

    with open(filename, 'r') as file:
        out = json.load(file)
