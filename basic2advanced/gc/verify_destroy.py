#!/usr/bin/bash

class A:
    def __del__(self):
        print("Destroyed")
    

a = A()
print("Change a refered")
a = 4

