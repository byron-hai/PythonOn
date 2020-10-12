import logging
import os
import random
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s (%(threadName)-10s) %(message)s', datefmt="%Y%m%d %H:%M:%S")

class Account:
    def __init__(self, acctid, value=0):
        self.id = acctid
        self.value = value

    def increase(self):
        time.sleep(0.01)
        self.value += 1

def job(c):
    logging.debug("Started")
    c.increase()
    logging.debug(c.value)
def add_with_lock(c, l):
    with l:
        c.increase()

acct = Account('001', 0)
threads = []
lock = threading.Lock()
for _ in range(10):
    threads.append(threading.Thread(target=job, args=(acct,)))

for td in threads:
    td.start()

for td in threads:
    td.join()

