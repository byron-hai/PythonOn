#!/bin/bash/env python3
# -*- coding:utf-8 -*-

import signal
import time

def alarm_handler(signum, stack):
    print("Alarm signal received at ", time.ctime())


signal.signal(signal.SIGALRM, alarm_handler)
signal.alarm(2)


print('Before: ', time.ctime())
time.sleep(4)
print('After: ', time.ctime())


