#!/usr/bin/env python3
"""
@ Desc:
@ Author: Byron
@ Date:
"""


class Array:
    def __init__(self, capacity, fill_value=None):
        self._items = list()
        [self._items.append(fill_value) for count in range(capacity)]

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, new_value):
        self._items[index] = new_value

