#!/usr/bin/env python3
"""
@ Desc: 
@ Author: Byron
@ Date: 
"""


class Grid:
    def __init__(self, rows, columns, value=None):
        self._data = []
        for i in range(rows):
            self._data.append([value for j in range(columns)])

    def get_height(self):
        return len(self._data)

    def get_width(self):
        return len(self._data[0])

    def find(self, val):
        for i in range(self.get_height()):
            for j in range(self.get_width()):
                if self._data[i][j] == val:
                    return i + 1, j + 1

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, key, value):
        self._data[key] = value

    def __str__(self):
        result = ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self._data[row][col]) + " "
            result += "\n"
        return result

