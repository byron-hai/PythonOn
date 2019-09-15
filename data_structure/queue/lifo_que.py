#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@ Desc:
  LIFO Queue: same with stack. put() is like push() in stack; get() is like pop() in stack
  The Constructor for a LIFO queue is as follows:

    class Queue.LifoQueue(maxsize=0)

  The queue size will be infinite if maxsize <= 0.

@ author: byron
@ Date: 2019-09-15
@ History: 
"""
from queue import LifoQueue


q = LifoQueue()
print("Queue size before put: ", q.qsize())

for i in range(10):
    print("put %d in queue" % i)
    q.put(i)

print("Queue size after  put: ", q.qsize())

while not q.empty():
    print(q.get())
