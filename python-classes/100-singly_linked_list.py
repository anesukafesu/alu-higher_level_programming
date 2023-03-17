#!/usr/bin/python3
"""This module defines the classes needed for a LinkedList

Example:
    my_list = SinglyLinkedList()
    my_list.sorted_insert(5)
    my_list.sorted_insert(4)
    print(my_list)
"""

class Node:
    """Implements a single node in a linked list
    """
    def __init__(self, data, next_node=None):
        """Implements Node
        Args:
            data (int): The value to be stored at that node
            next_node (Node): A pointer to the next node
        Returns:
            Node: The newly created node as it is a constructor
        """
        self.data(data)
        self.next_node(next_node)
    
    @property
    def data(self):
        """int: Returns the data stored by this node
        Returns:
            data (int): The value stored at this node
        """
        return self.__data

    @property
    def next_node(self):
        """Node: Returns the next_node in the list or None if there is no next_node and this node is the last in the list
        """
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
    """Implements a singly-linked list
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

