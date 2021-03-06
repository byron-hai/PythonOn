#!/usr/bin/env python3
"""
@ Desc: Quick sort works by choosing a pivot and partitioning the array so
that the elements that are smaller than the pivot goes to the left. Then,
it recursively sorts the left and right parts.
Time complexity: Best-Avg-Worst: O(n log(n), O(n log(n), O(n log(n)
@ Author: Byron
@ Date:
"""

import random


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        mid_index = (len(arr) - 1) // 2
        left_arr = [i for i in arr if i < arr[mid_index]]
        right_arr = [i for i in arr if i > arr[mid_index]]
        mid = [i for i in arr if i == arr[mid_index]]
        return quick_sort(left_arr) + mid + quick_sort(right_arr)


if __name__ == "__main__":
    arr = [random.randint(0, i) for i in range(1, 100)]
    print("Original array:\n%s\nlength: %d\n" % (str(arr), len(arr)))

    sorted_arr = quick_sort(arr)
    print("Sorted array:\n%s\nLength: %d\n" % (str(sorted_arr), len(sorted_arr)))
