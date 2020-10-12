#-*- coding:utf-8 -*-

# Find the shortest sub-string in a array which has sum equals to a given number

def min_sub_arr(lst, s):
    left = 0
    min_len = float('inf')
    sub_sum = 0
    for right in range(0, len(lst)):
        sub_sum +=lst[right]
        while sub_sum >= s:
            min_len = min(min_len, right - left + 1)
            sub_sum -= lst[left]
            left += 1

    return 0 if min_len == float('inf') else min_len


if __name__ == '__main__':
    tc_list = [(7, [2,3,1,2,4,3], 2),
               (15, [1,2,3,4,5], 5),
               (15, [5,1,3,5,10,7,4,9,2,8], 2),
               (28, [1,2,3,4,5], 0)]
    for tc in tc_list:
        s, lst = tc[:2]
        print("Testing: %d %s, Expect: %d" % (s, lst, tc[2]))
        rtn = min_sub_arr(lst, s)
        print(rtn)
