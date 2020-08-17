#!/usr/bin/env python3
"""
@ Desc: 
@ Author: Byron
@ Date: 
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self._head = None

    @property
    def is_empty(self):
        return False if self._head else True

    def length(self):
        count = 0
        cur = self._head
        while cur:
            cur = cur.next
            count += 1
        return count

    def head_add(self, item):
        new_node = Node(item)
        new_node.next = self._head
        self._head = new_node

    def append(self, item):
        new_node = Node(item)

        if self.is_empty:
            self.head_add(item)
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def travel(self):
        cur = self._head
        while cur:
            print(cur.data)
            cur = cur.next

    def insert(self, pos, item):
        pass

    def remove(self, item):
        pass

    def search(self, item):
        pass
