#!/usr/bin/env python3
"""
@ Desc: 
@ Author: Byron
@ Date: 
"""


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            raise LookupError("stack is empty")
        return self.stack.pop()

    def __str__(self):
        return str(self.stack)

    def is_empty(self):
        return False if self.stack else True  # A mistake if return bool(self.stack)

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        return self.stack[-1]

    def size(self):
        return len(self.stack)
