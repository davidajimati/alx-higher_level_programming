#!/usr/bin/python3
'''
THis module writes an Object to a text file,
using a JSON representation:
'''
import json


def save_to_json_file(my_obj, filename):
    ''' Saves a python object into a text file in JSON representation '''
    with open(filename, 'w', encoding="utf-8") as f:
        f = json.dumps(my_obj)
        print(f)
