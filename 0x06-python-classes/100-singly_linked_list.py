#!/usr/bin/python3
"""Singly Linked List

This module implements a singly linked list
as a Node class

Todo:
    * write a class Node that defines a node of a singly linked list.
    * write a class SinglyLinkedList that defines a singly linked list
"""


class Node:
    """Defines a node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initializes a node

        Args:
            data (int): node data.
            next_node (Node): an object to the next node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets the node data

        Returns:
            node data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the node data

        Args:
            value (int): the node data."""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets and returns object to next node.

        Returns:
            object to next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the object to next node.

        Args:
            value (Node): object to next node."""
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        """Initializes a Singly Linked List"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node to the singly linked list.

        Args:
            value (Node): object to next node."""
        if self.__head is None:
            self.__head = Node(value)
        elif self.__head.next_node is None:
            if value > self.__head.data:
                self.__head.next_node = Node(value)
            else:
                temp = self.__head
                self.__head = Node(value, temp)
        else:
            head = self.__head.next_node
            prev = self.__head

            while head.next_node is not None and head.data < value:
                prev = head
                head = head.next_node

            if prev.data > value:
                self.__head = Node(value, prev)
            elif head.next_node is None:
                if head.data > value:
                    prev.next_node = Node(value, head)
                else:
                    head.next_node = Node(value)
            else:
                prev.next_node = Node(value, head)

    def __str__(self):
        """Prints a singly linked list"""
        str = ""
        if self.__head is not None and self.__head.next_node is None:
            str += "{:d}".format(self.__head.data)
            if self.__head.next_node is not None:
                str += "\n"
        elif self.__head is not None and self.__head.next_node is not None:
            head = self.__head

            while self.__head is not None:
                str += "{:d}".format(self.__head.data)
                if self.__head.next_node is not None:
                    str += "\n"
                self.__head = self.__head.next_node

            self.__head = head

        return str
