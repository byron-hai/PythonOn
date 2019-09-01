#!/usr/bin/env python3
"""
@ Desc: 
@ Author: Byron
@ Date: 
"""
from LinkedList.singly_linkedList import Node, LinkedList


if __name__ == '__main__':
    a = [1, 2, 3, 5]
    b = ('sds', 'bb')
    c = "This is demo experiment"
    d = {'a': 'AAA', 'b': 'BBBB'}
    head = None
    llist = LinkedList()
    print(llist.is_empty)

    for item in [a, b, c, d]:
        llist.append(item)

    llist.travel()
    print(llist.search(a))

    llist.insert(3, "I'm at the third position")
    llist.travel()

    llist.remove(b) if llist.search(b) else None
    llist.travel()
