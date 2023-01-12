#!/usr/bin/python3
'''
This module writes into a specified file in UTF8
and returns the number of characters written
'''


def write_file(filename="", text=""):
    ''' Writes and returns the number of characters written '''
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
        return (len(text))
