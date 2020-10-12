import logging
import os
import random
import threading
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s (%(threadName)-10s) %(message)s', datefmt='%Y%m%d %H:%M:%S')

class Counter:
    def __init__(self, start=0):
        self.cnt = start
        self.lock = threading.Lock()

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('lock acquired')
            if self.cnt < 10:
                self.cnt += 1
        finally:
            self.lock.release()


def job(c):
    for i in range(2):
        pause = random.random()
        logging.debug("Sleeping %0.02f", pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Done')


counter = Counter()
threads = []
for _ in range(6):
    threads.append(threading.Thread(target=job, args=(counter,)))

for td in threads:
    td.start()
    
for td in threads:
    td.join()

logging.debug("Counter: %d", counter.cnt)

