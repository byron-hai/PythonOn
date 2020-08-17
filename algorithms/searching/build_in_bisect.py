#!/usr/bin/env python3
"""
@ Desc: Python’s built-in bisect() module is available for binary search in a sorted sequence
@ Author: Byron
@ Date: 
"""
from bisect import bisect

tc_list = [23, 45, 12, 45, 36, 75, 42, 65]
print(bisect(sorted(tc_list), 23))
