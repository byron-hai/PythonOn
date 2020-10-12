#-*- coding:utf-8 -*-

import multiprocessing as mp
import os

def worker():
    print(os.getpid(), mp.current_process().name)


if __name__ == "__main__":
    ps_list = []
    for i in range(5):
        ps_list.append(mp.Process(target=worker))

    for p in ps_list:
        p.start()



