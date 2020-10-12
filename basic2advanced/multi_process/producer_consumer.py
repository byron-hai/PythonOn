import multiprocessing as mp
import time
import random

class Task:
    def __init__(self, task_num, content, run_time):
        self.num = task_num
        self.content = content
        self.run_time = run_time

    def run(self, result_q):
        print("Starting task-{}: {}".format(self.num, self.content))
        time.sleep(self.run_time)
        print("Ending task-{}".format(self.num))
        result_q.put("Task-{} done in {} seconds".format(self.num, self.run_time))


def producer(task_q, resource, num, lock):
    while resource:
        with lock:
            if resource:
                mat = resource.pop(0)
                num.value += 1
                prod_id = num
                print("Producing product-{}{}".format(mp.current_process().name, num.value))
                time.sleep(random.random() + 0.5)
                task = Task(num.value, mat, len(mat) // 3)
                task_q.put(task)
            else:
                break
    print("No resources")
    task_q.put(None)


def consumer(task_q, result_q):
    while True:
        task = task_q.get(timeout=5)
        if task == None:
            break

        print("{}: Got task-{}".format(mp.current_process().name, task.num))
        task.run(result_q)
        task_q.task_done()

if __name__ == "__main__":

    #task_q = mp.Queue()
    #result_q = mp.Queue()
    mgr = mp.Manager()
    task_q = mp.JoinableQueue()
    result_q = mgr.Queue()
    lock = mgr.Lock()
    number = mgr.Value('i', 0)
    resources = mgr.list(["dvdvd", "grgt53xc",  "wgrwgrg", "vqgrqegreq", "efe  tegeg", "ee rgg"])
    works = []
    cons_works = []

    for line in ['A']:
        prod = mp.Process(name=line, target=producer, args=(task_q, resources, number, lock))
        works.append(prod)
        prod.start()

    for i in range(4):
        consumer = mp.Process(target=consumer, args=(task_q, result_q))
        works.append(consumer)
        consumer.start()

    for work in works:
        work.join()

    while not result_q.empty():
        print(result_q.get())
