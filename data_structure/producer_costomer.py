#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@ Desc:
@ author: byron
@ Date: 2019-09-15
@ History: 
"""
import threading
import time
import queue

TIME_FMT = '%H:%M:%S'


def customer(q):
    while True:
        name = threading.current_thread().getName()
        print("Thread: {}, get item from queue.  Current queue size: {}, Time: {}".
              format(name, q.qsize(), time.strftime(TIME_FMT)))
        if q.empty():
            print("No task in queue.")
            break
        else:
            item = q.get()

        time.sleep(1)
        print("Thread: {}, {} finished.  Current queue size: {}, Time: {}".
              format(name, item, q.qsize(), time.strftime(TIME_FMT)))


def producer(q):
    for i in range(10):
        name = threading.current_thread().getName()
        item = "task-" + str(i)
        print("Thread: {}, put item '{}' in queue.  Current queue size: {}, Time: {}".
              format(name, item, q.qsize(), time.strftime(TIME_FMT)))
        q.put(item)


q = queue.Queue()
t1 = threading.Thread(target=producer, args=(q, ))
t2 = threading.Thread(target=customer, args=(q, ))

t1.start()
t2.start()
t1.join()
t2.join()

