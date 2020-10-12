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

def daemon_worker():
    print(os.getpid(), mp.current_process().name)

def worker():
    print(os.getpid(), mp.current_process().name)

if __name__ == "__main__":

    work1 = mp.Process(target=worker1, args=(2,))
    work2 = mp.Process(target=worker2, args=(6,))
    work1.start()
    work2.start()
    work2.join(2)
    print("Main process")
    print("Process Work2 alive? ", work2.is_alive())



