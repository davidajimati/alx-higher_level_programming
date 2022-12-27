#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
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
            if type(value) != type(Node) and value != None:
                raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            return

        trav = self.head
        while trav.next_node and trav.data < value:
            if value > trav.data:
                node.next_node = trav.next_node
                trav.next_node = node
                return

            if value < self.head.data:
                node.next_node = self.head
                self.head = node
                return

            trav = trav.next_node
        trav.next_node = node

    def __str__(self):
        ret = ""
        read = self.head

        while read:
            ret += str(read.data) + '\n'
            read = read.next_node
        return ret[:-1]


sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)
