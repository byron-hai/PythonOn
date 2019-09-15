#!/usr/bin/env python3
"""
@ Desc: 
@ Author: Byron
@ Date: 
"""


from pyStack import Stack
brackets_left = "([{"
brackets_right = ")]}"
math_symbols = "+-*/"


def syntax_check(string):
    back_string = ""
    brackets = Stack()

    for i in string:
        print(brackets)
        if i in brackets_left:
            brackets.push(i)
        elif i in brackets_right:
            print(brackets.size())
            j = brackets.pop()
            if brackets_left.index(j) != brackets_right.index(i):
                raise SyntaxError("'%s' got no matched part at position %d" % (i, string.index(i)))

    if not brackets.is_empty:
        print("Size: ", brackets.size())
        raise SyntaxError("brackets not matched. ")
    return True


if __name__ == "__main__":
    math_str = "(2 + 4) * [68 / (3 + 20)]"
    math_str2 = "{[3 * 6] / 8 -4 )} * 2"

    syntax_check(math_str)
    print("Check over: ", math_str)
    syntax_check(math_str2)
    print("Check over: ", math_str2)
