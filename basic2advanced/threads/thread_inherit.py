# -*- coding:utf-8 -*-

import threading 
import time

class MyThread(threading.Thread):
    def __init__(self, param=None, sleep=1):
        super().__init__()
        self.param = param
        self.sleep = sleep

    def run(self):
        time.sleep(self.sleep)
        print("In MyThread", self.param)


def main():
    td = MyThread("Hello", 3)

    td.start()

if __name__ == '__main__':
    main()
