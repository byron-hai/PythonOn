#!/usr/bin/env python3

# 5! = 5 * 4 * 3 * 2 * 1
def fact(num):
    return 1 if num == 1 else num * fact(num - 1)



