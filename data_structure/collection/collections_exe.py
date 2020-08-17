#!/usr/bin/env python3
"""
@ Desc: 
@ Author: Byron
@ Date: 
"""
from collections import Counter


def find_top_n_recurring_words(string, n):
    counter = Counter()
    for word in string.split():
        counter[word] += 1
    return counter.most_common(n)


def find_top_n_recurring_words2(string, n):
    counter = {}
    for word in string.split():
        if word in counter.keys():
            counter[word] += 1
        else:
            counter[word] = 1
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)[:n]

