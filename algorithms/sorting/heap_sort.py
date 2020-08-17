#!/usr/bin/env python3
"""
@ Desc:  In python, a heap sort can be implemented by pushing all values onto a heap
         and then popping oﬀ the smallest values one at a time
         Time Complexity: Best-Avg-Worst: O(n log(n), O(n log(n), O(n log(n)
@ Author: Byron
@ Date: 
"""
import heapq


def heap_sort(seq):
    h = []
    for value in seq:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


def test_heap_sort():
    seq = [4, 6, 8, 2, 6, 9, 1, 7, 3]
    assert(heap_sort(seq) == sorted(seq))
    print(heap_sort(seq))


if __name__ == '__main__':
    test_heap_sort()
