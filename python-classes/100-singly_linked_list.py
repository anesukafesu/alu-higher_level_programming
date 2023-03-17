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
        self.__set_data(data)

        # Initially the node can be none
        self.__next_node = next_node
    
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
        self.__set_data(value)

    def __set_data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')

        self.__data = value

    @next_node.setter
    def next_node(self, value):
        self.__set_next_node(value)

    def __set_next_node(self, value):
        if not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

    def __repr__(self):
        return f'{self.data}'


class SinglyLinkedList:
    """Implements a singly-linked list
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a value in a sorted manner into the list
        Args:
            value (int) The value to be inserted
        Returns:
            None
        """
        new_node = Node(value)
        
        # If the list is empty
        if self.__head == None:
            self.__head = new_node
        elif self.__head.data > new_node.data:
            if self.__head.next_node != None:
                new_node.next_node = self.__head.next_node
            
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            prev = self.__head
            curr = self.__head.next_node
            # This will stop when we 
            # a. Encounter a value bigger than the value we want to add
            # b. We run out of nodes
            while curr != None and curr.data < new_node.data:
                prev = curr
                curr = curr.next_node
            
            new_node.next_node = curr
            prev.next_node = new_node


    def __repr__(self):
        output = ""
        node = self.__head
        
        while True:
            if node == None:
                break
            else:
                output += f'{node}\n'
                node = node.next_node
        return output.rstrip()
