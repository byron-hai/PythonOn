# -*- coding:utf-8 -*-

import multiprocessing as mp

def worker(num, share_dict, q):
    share_dict[num] = num ** 2
    q.put(num)

if __name__ == "__main__":

    share_d = mp.Manager().dict()
    test_q = mp.Queue()

    ps_all = []
    for i in range(5):
        ps_all.append(mp.Process(target=worker, args=(i, share_d, test_q)))

    for ps in ps_all:
        ps.start()

    for ps in ps_all:
        ps.join()

    print(share_d)
    print([test_q.get() for i in range(test_q.qsize())])
