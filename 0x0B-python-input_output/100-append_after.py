#!/usr/bin/python3

'''
inserts a line of text to a file,
after each line containing a specific string (
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    Searches "filename" for "search_string"
    and appends "new_string_ after it
    '''
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in range(len(lines)):
        if search_string in lines[line]:
            lines[line] = (lines[line] + new_string)

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
