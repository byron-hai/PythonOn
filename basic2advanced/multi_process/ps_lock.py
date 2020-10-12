# -*- coding:utf-8 -*-

import multiprocessing as mp

def worker(num, l):
    print("%s: Before: %d" % (mp.current_process().name, num))
    with l:
        if num > 10:
            num += 2
        else:
            num -= 3

    print("%s: After: %d" % (mp.current_process().name, num))

if __name__ == "__main__":

    lock = mp.Lock()
    ls = mp.Manager().list()

    ps_all = []

    for _ in range(2):
        ps_all.append(mp.Process(target=worker, args=(ls, lock)))

    for ps in ps_all:
        ps.start()

    for ps in ps_all:
        ps.join()

    print(num)
