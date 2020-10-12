#-*- coding:utf-8 -*-

import multiprocessing as mp
import logging
import os
import time

logging.basicConfig(level=logging.DEBUG, 
                    format="%(asctime)s %(message)s",
                    datefmt="%Y%m%d %H:%M%S")

def worker1(num):
    logging.debug(mp.current_process().name + " Started")
    time.sleep(num)
    logging.debug(mp.current_process().name + " Ended")

def worker2(num):
    logging.debug(mp.current_process().name + " Started")
    time.sleep(num)
    logging.debug(mp.current_process().name + " Ended")

def daemon_worker(num):
    logging.debug(mp.current_process().name + " Started")
    for i in range(10):
        print(i)
        time.sleep(1)
    logging.debug(mp.current_process().name + " Ended")

def worker():
    print(os.getpid(), mp.current_process().name)

if __name__ == "__main__":

    work1 = mp.Process(target=worker1, args=(4,))
    work2 = mp.Process(target=daemon_worker, args=(10,), daemon=True)
    # work2.daemon = True
    work1.start()
    work2.start()
    work1.join()
    work2.join(2)
    print("Main process")
    print("Process Work2 alive? ", work2.is_alive())



