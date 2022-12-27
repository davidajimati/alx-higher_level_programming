# Excellence or Nothing!

class Node:
    def __init__(self, data=None, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        self.data = data

        if type(next_node) is not type(Node):
            raise TypeError("next_node must be a Node object")
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def sorted_insert(self, data):
        # trav = self.head
        if self.head == None:
            self.data = data
        else:
            while self.head is not None:
                if data > self.head.data:
                    self.head = self.head.next
                else:
                    self.head.data = data

                node = Node(self.head.data, self.head.next)
                self.head = node

    def print(self, llist):
        # if llist.head == None:
        #     print("linked list empty!")

        trav = llist.head
        while trav is not None:
            print(trav.data)
            trav = trav.next

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
sll.print(sll)