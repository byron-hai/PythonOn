#!/usr/bin/env python3
"""
@ Desc: 
@ Author: Byron
@ Date: 
"""

import random
import time


def binary_search(lst, item):
    index_min = 0
    index_max = len(lst) - 1

    while index_min <= index_max:
        mid = (index_min + index_max) // 2
        guess = lst[mid]
        if item == guess:
            return mid
        elif guess > item:
            index_max = mid
        else:
            index_min = mid

    return None


if __name__ == '__main__':
    for num in [1000, 10000, 1000000, 1000000000]:
        guest_list = range(1, num)
        guess_num = random.randint(1, num)
        print("Guess num game: list length: " + str(num))
        start = time.clock()
        pos = binary_search(guest_list, guess_num)
        end = time.clock()
        print("Found you!. Number: %d at %d, time: %f" % (guess_num, pos, end - start))
