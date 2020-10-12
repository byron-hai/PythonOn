#-*- coding:utf-8 -*-
import threading
import queue
import logging
import random
import time

def consumer(task_q, cond):
    logging.debug('Starting consumer thread')
    ck_limit = 2
    ck = 0
    while True:
        cond.acquire()
        if task_q.qsize() > 0:
            task = task_q.get()
            task_cont, exe_time = task
            logging.info("Executing %s. Start-time %s", task, time.ctime())
            time.sleep(exe_time)
            logging.info("%s finished. End-time: %s", task, time.ctime())
            cond.notify()
        else:
            logging.info("No tasks. Waiting..")
            ck += 1
            if ck == ck_limit:
                cond.release()
                break
            cond.wait(3)
        cond.release()

    return 

def producer(resources, task_q, cond):
    logging.debug("Starting producer thread")
    cnt = 0
    while resources:
        with cond:
            if task_q.qsize() < 5:
                resource = resources.pop(0)
                task, produce_time = resource[:2], resource[-1]
                time.sleep(produce_time)
                task_q.put(task)
                cnt += 1
                logging.debug("Task %d is ready, took time %d", cnt, produce_time)
                cond.notifyAll()
            else:
                cond.wait()

    logging.info("Resource over.")


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s (%(threadName)-2s) %(message)s',)

task_q, consumer_q = queue.Queue(), queue.Queue()
cond = threading.Condition()
consumers = 3
resource_cnt = 10

for i in range(consumers):
    consumer_q.put(i)

resources = [] # Item ('task-name', exe-time, produce-time)
for i in range(resource_cnt):
    resources.append(("Task-" + str(i), random.randint(2,5), random.randint(1,4)))

threads = []
threads.append(threading.Thread(name='Producer', target=producer, args=(resources, task_q, cond)))

for i in range(consumers):
    threads.append(threading.Thread(name='Consumer-' + str(i), target=consumer, args=(task_q, cond)))

for td in threads:
    td.start()

for td in threads:
    td.join()

print(threading.active_count())
