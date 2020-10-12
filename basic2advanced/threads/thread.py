import os
import threading
import time

def job1(i):
    print("{} Job: {}, Started. PID: {}".format(time.strftime("%Y%M%d %H:%M:%S", time.gmtime()), 
                                                 threading.current_thread().getName(), os.getpid()))
    time.sleep(i)
    print("{} Job: {}, Finished".format(time.strftime("%Y%M%d %H:%M:%S", time.gmtime()), 
                                        threading.current_thread().getName()))

def job2(j):
    print("{} Job: {}, Started. PID: {}".format(time.strftime("%Y%M%d %H:%M:%S", time.gmtime()), 
                                                 threading.current_thread().getName(), os.getpid()))
    time.sleep(j)
    print("{} Job: {}, Finished".format(time.strftime("%Y%M%d %H:%M:%S", time.gmtime()), 
                                        threading.current_thread().getName()))    

if __name__ == '__main__':
    t1 = threading.Thread(target=job1, args=(2,))      
    t2 = threading.Thread(target=job2, args=(4,))
    t1.start()
    t2.start()
    print("Current PID: ", os.getpid())
