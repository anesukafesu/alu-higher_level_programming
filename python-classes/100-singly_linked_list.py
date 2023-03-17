#!/usr/bin/python3
"""
This module defines the classes needed for a LinkedList
It contains the class Node
which stores a value and a reference to the next node
It also stores the class SinglyLinkedList
which is used for list-wide operations
such as inserting new nodes and getting all nodes
"""

class Node:
    """
    class Node
    stores value as data
    stores a reference to the next node in next_node
    if it is the terminal node then next_node will be none
    """
    def __init__(self, data, next_node=None):
        self.data(data)
        self.next_node(next_node)
    
    @property
    def data(self):
        return self.__data

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')

        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')

    def __repr__(self):
        return self.data()


class SinglyLinkedList:
    """
    implements a linked list
    allows simple operations like inserting items
    and printing out values into the terminal
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head = None:
            self.__head = Node(value)
        else:
            # We maintain a pointer to the previous node for adding
            prev = self.__head

            curr = self.__head.next_node

            while True:
                if curr == None:
                    prev.next_node = Node(value)
                    break
                else:
                    prev = curr
                    curr = curr.next_node

    def __repr__(self):
        output = ""
        node = self.__head
        
        while True:
            if node == None:
                break
            else:
                output += f'{node}\n'
                node = node.next

