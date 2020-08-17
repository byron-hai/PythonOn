#!/usr/bin/env python3
"""
@ Desc:  ﬁnds the position of a speciﬁed input value (the key) within a sorted array.
         In each step, the algorithm compares the search key value with the key value
         of the middle element of the array.
         O(lnn)
@ Author: Byron
@ Date: 
"""

import random
import time


# Recursive
def binary_search_rec(seq, target):
    mid = len(seq) // 2  # for int type, always use //
    if target == seq[mid]:
        return mid
    elif target > seq[mid]:
        return binary_search_rec(seq[mid:], target)
    else:
        return binary_search_rec(seq[:mid], target)


# Iterative
def binary_search_iter(lst, item):
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

def test_binary_search():
    for num in [1000, 10000, 1000000]:
        guest_list = list(range(1, num))
        guess_num = random.randint(1, num)
        print("Guess num game: list length: " + str(num))
        start1 = time.clock()
        pos = binary_search_iter(guest_list, guess_num)
        end1 = time.clock()
        print("Search iteratively!. Number: %d at %d, time: %f" % (guess_num, pos, end1 - start1))

        start2 = time.clock()
        pos2 = binary_search_rec(guest_list, guess_num)
        end2 = time.clock()
        print("Search recursively!. Number: %d at %d, time: %f" % (guess_num, pos, end2 - start2))


if __name__ == '__main__':
    test_binary_search()
