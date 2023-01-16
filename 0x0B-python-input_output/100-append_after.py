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
    with open(filename, 'r+') as file:
        for line in file:
            if search_string in line:
                line = line.rstrip()
                file.write(line.replace(line, new_string))
                print (line)



append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")