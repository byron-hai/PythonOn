#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
@ Desc:
@ author: byron
@ Date: 2019-09-02
@ History: 
"""
import random


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    print(arr)
    for i in range(0, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def select_sort(arr):
    new_arr = []

    for i in range(len(arr)):
        new_arr.append(arr.pop(find_smallest(arr)))

    return new_arr


if __name__ == '__main__':

    raw = [random.randint(1, i * 100) for i in range(1, 100)]
    print("Raw list:\n" + str(raw))
    print("SelectionSorted list:\n" + str(select_sort(raw)))
