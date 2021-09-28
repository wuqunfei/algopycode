"""
https://realpython.com/linked-lists-python/
"""


class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class LinkedList:

    def __init__(self):
        self.head: Node = None

    def insert(self, data):
        node = Node(data=data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            self.head = current
        else:
            self.head = node


l = LinkedList()
l.insert(1)
l.insert(2)
l.insert(3)
