# -*- coding:utf-8 -*-

import signal
import threading
import os
import time

def signal_handler(num, stack):
    print('Received signal {} in {}'.format(num, threading.current_thread().getName()))

signal.signal(signal.SIGUSR1, signal_handler)

def wait_for_signal():
    print("Waiting for signal in ", threading.current_thread().getName())
    signal.pause()
    print("Waiting done")
    

def send_signal():
    print("Sending signal in ", threading.current_thread().getName())
    os.kill(os.getpid(), signal.SIGUSR1)

receiver = threading.Thread(target=wait_for_signal, name='receiver')
sender = threading.Thread(target=send_signal, name='sender')

receiver.start()
time.sleep(0.1)
sender.start()
sender.join()
print('Waiting for ', receiver.name)
signal.alarm(2)
receiver.join()
