#!/usr/bin/python3
'''
This module opens a file in UTF8 and
prints its content to stdout
'''


def read_file(filename=""):
    ''' Reads filename as file '''
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
