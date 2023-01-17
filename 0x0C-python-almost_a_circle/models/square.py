#!/usr/bin/python3

'''
Module contains a subclass that inherits from Rectangle
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Constructor'''

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))

    @property
    def size(self):
        return(self.size)

    @size.setter
    def size(self, value):
        self.size = value