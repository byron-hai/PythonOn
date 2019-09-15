#!/usr/bin/env python3
"""
@ Desc: 
@ Author: Byron
@ Date: 
"""
from pyStack import Stack


def decimal_to_bin(dec):
    stack = Stack()
    cur = dec

    if type(dec) != int:
        raise TypeError("Input must be a number")

    while cur > 0:
        rem = cur % 2
        cur = cur // 2
        stack.push(rem)

    bin_rtn = ""
    while not stack.is_empty():
        bin_rtn += str(stack.pop())  # Be careful on type

    return bin_rtn


if __name__ == '__main__':
    print(decimal_to_bin(7))
    print(decimal_to_bin(80))
