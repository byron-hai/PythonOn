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

    def __repr__(self):
        return str(self.data)


def print_list(node):
    while node:
        print(node)
        node = node.next


def add(node, node_new, pos=0):
    if pos == 0:
        node_new.next = node
        return node_new
    elif pos and type(pos) == int:
        index = 0
        while node.next and index != pos:
            node = node.next

        if node:
            node_tmp = node
            node.data = node_new.data
            node.next = node_tmp
        else:
            node = node_new
            return node_new


def delete(node, val):
    while node:
        if val == node.data:
            node.data = None
        else:
            node = node.next
    return False


def change(node, val_old, val_new):
    while node:
        if val_old == node.data:
            node.data = val_new
            return val_new
        else:
            node = node.next
    return False


def search(node, val):
    index = 0
    while node:
        if val == node.data:
            print("Found %s at %d" % (val, index))
            return index, val
        else:
            node = node.next
        index += 1
    return False


if __name__ == '__main__':

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    node1.next = node2
    node2.next = node3

    head = node1
    print_list(head)
    search(head, 2)

    print("Change")
    head = node1
    change(head, 2, 5)
    head = node1
    print_list(head)

    print_list(head)
    print("After")
    node_new = Node("34")
    head = add(node1, node_new)
    print_list(head)
