#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@ Desc:
  FIFO: Items can be added to the end of the container using put(), and removed from the head using get()
  The constructor for a FIFO queue is as follows:

    class Queue.Queue(maxsize=0)

  Insertion will be blocked once the queue is full, until items are consumed.
  The queue size is infinite if maxsize <= 0.

  Most important methods: put(), get() and join(), task_done() and join()
  Queue.put(item[, block[, timeout]])
  Queue.put_nowait(item) / Queue.get([block[, timeout]])
  Queue.get_nowait()

  Queue.join()  # Blocks until all items in the queue have been gotten and processed.
  Queue.qsize()
  Queue.empty() # Return True if the queue is empty, False otherwise

@ author: byron
@ Date: 2019-09-15
@ History: 
"""


from queue import Queue


q = Queue()
print("Queue size before put: ", q.qsize())

for i in range(10):
    q.put(i)

print("Queue size after  put: ", q.qsize())

while not q.empty():
    print(q.get())
