#!/usr/bin/python3
class Node:
    '''
    Declaration of a singly linked list node structure
    Python Implementation.
    '''

    def __init__(self, data, next_node=None):
        '''
        Class constructor
        '''
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, value):
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            if type(value) != type(Node) and value is not None:
                raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    '''
    Definition of a node of the linked list
    '''

    def __init__(self):
        '''initiator (constructor)
        '''
        self.head = None

    def sorted_insert(self, value):
        '''
        This function inserts nodes and arranges them in
        ascending order of their data (integers)
        '''
        new = Node(value)
        if not self.head:
            self.head = new
            return

        if value < self.head.data:
            new.next_node = self.head
            self.head = new
            return

        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        if node.next_node:
            new.next_node = node.next_node
        node.next_node = new

    def __str__(self):
        '''
        method to modify the print function
        '''
        ret = ""
        read = self.head

        while read:
            ret += str(read.data) + '\n'
            read = read.next_node
        return ret[:-1]
