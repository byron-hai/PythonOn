#!/usr/bin/env python3
"""
@ Desc: Sort by repeatedly inserting the next unsorted element
        in an initial sorted segment of the array
        Best runtime: O(n)
        Worst runtime: O(n^2)
@ Author: Byron
@ Date: Dec.19 2019
"""


def insertion_sort1(seq_list):
    for i in range(1, len(seq_list)):
        for j in range(0, i):
            if seq_list[i] < seq_list[j]:
                seq_list[i], seq_list[j] = seq_list[j], seq_list[i]

    return seq_list


def insertion_sort2(seq_list):
    for i in range(1, len(seq_list)):
        j = i
        while j > 0 and seq_list[j] > seq_list[i]:
            seq_list[j], seq_list[i] = seq_list[i], seq_list[j]
            j -= 1
    return seq_list


def test_insertion_sort():
    seq = [33, 15, 22, 8, 37, 26, 11, 39]
    print("By insertion_sort: ", insertion_sort1(seq))
    print("By insertion_sort: ", insertion_sort2(seq))
    print("By sorted: ", sorted(seq))
    assert(insertion_sort1(seq) == sorted(seq))

    print('Test passed')


if __name__ == '__main__':
    test_insertion_sort()
