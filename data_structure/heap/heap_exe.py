#!/usr/bin/env python3
"""
@ Desc:  Heaps are binary trees for which every parent node has a value less than or equal
to any of its children. The interesting property of a heap is that its smallest element is
always the root, heap[0].
@ Author: Byron
@ Date:
@ Refer: https://docs.python.org/3.4/library/heapq.html
"""
import heapq

list1 = [2, 3, 7, 4, 8, 6]
heapq.heapify(list1)
print(list1)
heap = []

for num in range(10, 20):
    heapq.heappush(heap, num)

print(heap[0])

heapq.heappop(heap)
heap_new = heapq.merge(heap, list1)
for i in heap_new:
    print(i)


