#!/usr/bin/env python3
"""
@ Desc: 
@ Author: Byron
@ Date: 
"""

from pyStack import Stack


def check_symmetry(word):
    stack = Stack()
    if not len(word) % 2 == 0:
        print("Length of '%s' is odd" % word)
        return False

    for i in range(len(word) // 2):
        stack.push(word[i])

    for i in range(len(word) // 2, len(word)):
        letter = stack.pop()
        if letter != word[i]:
            print("Not a symmetry word. Position: %s, %s" % (letter, word[i]))
            return False
    return True


if __name__ == "__main__":
    word1 = 'noon'
    word2 = 'foot'

    for item in [word1, word2]:
        if check_symmetry(item):
            print(item + " is symmetry")
        else:
            print(item + " is not symmetry")
