#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@ Desc:
  PriorityQueue: the order of items in a queue are determined based on their importance or priority.
  Insertion will block once queue is full, until queue items are consumed . The queue size is infinite
  if the maxsize is negative or zero

  The constructor of python PriorityQueue is as follows:

    class Queue.PriorityQueue(maxsize=0)

  Please note that: The lowest valued entries are retrieved first.
  A typical pattern for entries is a tuple in this form: (the_priority_number, data_value).

@ author: byron
@ Date: 2019-09-15
@ History: 
"""

from queue import PriorityQueue

q = PriorityQueue()

tasks = [(2, "Get up"), (3, "Get to bank"), (1, "take keys"), (3, "take food"), (5, "Walk with dogs")]

for task in tasks:
    print("Put %s in queue" % str(task))
    q.put(task)

while not q.empty():
    print(q.get())
