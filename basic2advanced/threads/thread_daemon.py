import os
import threading
import time

def job(i):
    print("{} Job: {}, Started. PID: {}".format(time.strftime("%Y%M%d %H:%M:%S", time.gmtime()), 
                                                threading.current_thread().getName(), os.getpid()))
    time.sleep(i)
    print("{} Job: {}, Finished".format(time.strftime("%Y%M%d %H:%M:%S", time.gmtime()), 
                                        threading.current_thread().getName()))

def job_daemon(j):
    print("{} Job: {}, Started. PID: {}".format(time.strftime("%Y%M%d %H:%M:%S", time.gmtime()), 
                                                threading.current_thread().getName(), os.getpid()))
    time.sleep(j)
    print("{} Job: {}, Finished".format(time.strftime("%Y%M%d %H:%M:%S", time.gmtime()), 
                                        threading.current_thread().getName()))    

if __name__ == '__main__':
    t1 = threading.Thread(name='job', target=job, args=(2,))      
    t2 = threading.Thread(name='daemon_job', target=job_daemon, args=(4,), daemon=True)
    t1.start()
    t2.start()

