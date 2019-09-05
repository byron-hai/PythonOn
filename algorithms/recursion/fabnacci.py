#!/usr/bin/env python3

def fab(num): 
    if num <= 0: 
        raise ValueError("input must be greater than 0") 
    else: 
        return 1 if num < 3 else fab(num - 1) + fab(num - 2)
