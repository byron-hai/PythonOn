#!/usr/bin/env python3
"""
@ Desc:

Reference: https://www.mytecbits.com/internet/python/list-list-should-not-be-used-to-copy
@ Author: Byron
@ Date: 
"""
# Tip1: Do not use list = list to copy or clone a list. Use list.copy() instead
list_org = ["A", "B", "C", "D"]
list_cp1 = list_org
list_cp2 = list_org.copy()
print("list_org: %s, copied list by '=': %s" % (list_org, list_cp1))

list_cp1.remove("C")
list_cp1.append("F")
print("list_org: %s, copied list by '=' after remove 'C' and append 'F': %s" % (list_org, list_cp1))
print("list_org: %s, copied list by copy: %s" % (list_org, list_cp2))
