#!/usr/bin/python3

''' Creation of a class that inherits the properties
    of int
'''


class MyInt(int):
    def __eq__(self, object) -> bool:
        return not int.__eq__(self, object)

    def __ne__(self, object) -> bool:
        return not int.__ne__(self, object)
