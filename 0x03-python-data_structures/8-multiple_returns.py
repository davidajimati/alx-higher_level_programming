#!/usr/bin/python3
# returns length of string and its first character.

def multiple_returns(sentence):
    length = len(sentence)
    if len(sentence) == 0:
        char = None
    else:
        char = sentence[0]

    return (length, char)
