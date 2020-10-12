import multiprocessing as mp
import time, os

def callback_func(info):
    print("Callback: ", info)

def worker(num):
    print("Worker {} running, pid: {}".format(num, os.getpid()))
    time.sleep(1)
    return num * num


if __name__ == "__main__":
    pool = mp.Pool(os.cpu_count() * 2)
    res = []
    for i in range(7):
        res.append(pool.apply_async(worker, args=(i,), callback=callback_func))

    pool.close()
    pool.join()

    for i in res:
        print(i.get())

