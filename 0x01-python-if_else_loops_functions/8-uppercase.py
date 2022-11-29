#!/usr/bin/python3
def uppercase(str):
    string = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = ord(char) - 32
            char = chr(char)
            string = string + char
        else:
            string = string + char

    print(string)
