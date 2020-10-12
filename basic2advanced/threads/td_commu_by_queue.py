import time
import random
from threading import Thread, current_thread, Condition
from queue import Queue

# que = Queue() # 这里定义的que可以在线程里直接调用

class Consumer(Thread):
    def __init__(self, que):
        super().__init__()
        self.que = que

    def run(self):
        with cond:
            while self.que.qsize() == 0:
                cond.wait()

            item = self.que.get()
            print(f"{current_thread().getName()} got: ", item)

        print("Empty queue")

    
class Producer(Thread):
    def __init__(self, que):
        super().__init__()
        self.que = que

    def run(self):
        for _ in range(20):
            with cond:
                self.que.put(random.randint(1, 20))
                time.sleep(0.2)
                cond.notify_all()
            
if __name__ == "__main__":
    que = Queue()
    cond = Condition()

    threads = []
    threads.append(Producer(que))
    threads += [Consumer(que) for i in range(8)]

    for td in threads:
        td.start()
    
    #for td in threads:
    #    td.join()
