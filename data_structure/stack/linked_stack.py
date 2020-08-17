#!/usr/bin/env python3
"""
@ Desc: 
@ Author: Byron
@ Date: 
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return False if self.top else True

    def pop(self):
        node = self.top
        if node:
            self.top = node.next
            return node.value
        else:
            raise LookupError("stack is empty")

    def push(self, value):
        node = Node(value=value)
        node.next = self.top
        self.top = node

    def size(self):
        node = self.top
        num = 0
        while node:
            num += 1
            if not self.isEmpty():
                node = node.next
            else:
                break
        return num

    def peek(self):
        if not self.isEmpty():
            return self.top.value
        else:
            raise LookupError("stack is empty")


if __name__ == '__main__':
    stack = LinkedStack()
    for i in range(4):
        stack.push(i)

    print(stack.size())
    print(stack.peek())
    print(stack.pop())
    print(stack.peek())
    print(stack.size())
