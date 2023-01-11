#!/usr/bin/python3
'''
Module to append input to an existing file
'''


def append_write(filename="", text=""):
    ''' Appends to a new file or create  a new one'''
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
        return (len(text))
