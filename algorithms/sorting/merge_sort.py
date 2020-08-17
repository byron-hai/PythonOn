#!/usr/bin/env python3
"""
@ Desc: Merge sort divides the list in half to create two unsorted lists.
  These two unsorted lists are sorted and merged by continually calling
  the merge-sort algorithm, until you get a list of size 1.  The best,
  average, and worst case times are all O(nlnn)
@ Author: Byron
@ Date: 
"""


def merge_n1(left, right):
    if not left or not right:
        return left or right

    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):    # Max index of left
        result += left[i:]
    elif j < len(right):
        result += right[j:]

    return result


def merge_n2(left, right):
    if not left or not right:
        return left or right

    result = []
    while left and right:
        if left[-1] >= right[-1]:
            result.append(left.pop())
        else:
            result.append(right.pop())
    result.reverse()
    return (left or right) + result


def merge_sort(seq):
    if len(seq) < 2:
        return seq
    else:
        mid = len(seq) // 2
        left = merge_sort(seq[:mid]) if seq[:mid] else None
        right = merge_sort(seq[mid:]) if merge_sort(seq[mid:]) else None
        return merge_n2(left, right)


if __name__ == '__main__':
    seq1 = [45, 42, 12, 24, 67, 34, 28, 54]
    seq2 = [12, 34, 23, 45, 67, 23, 39]

    print(merge_sort(seq1))
    print(merge_sort(seq2))
