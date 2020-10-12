import multiprocessing as mp
import time

class TcProcess(mp.Process):
    def __init__(self, name):
        super().__init__()
        self.ps_name = name

    def run(self):
        print(self.ps_name + " is running")
        time.sleep(2)
        print(self.ps_name + " is finished")


if __name__ == '__main__':
    p = TcProcess("my_ps")
    p.start()

