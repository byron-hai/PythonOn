#-*- coding:utf-8 -*-

class Solution:
    def minSubArrayLen(self, s, nums):
        i, j = 0, 1
        min_len = 0
        nums_len = len(nums)
        while i < nums_len - 1 and j <= nums_len:
            sub = nums[i:j]
            if sum(sub) >= s:
                min_len = min(len(sub), min_len) if min_len != 0 else len(sub)
                print((i, j), sub, min_len)
                i += 1
                sub = nums[i:j]
                while sum(sub) >= s and i < j:
                    print((i, j), sub)
                    min_len = min(len(sub), min_len) if min_len != 0 else len(sub)
                    i += 1
                    sub = nums[i:j]
            else:
                j += 1 

        return min_len

def test(s, lst):
    solution = Solution()
    n = solution.minSubArrayLen(s, lst)
    print(n)

if __name__ == '__main__':
    tc_list = [(7, [2,3,1,2,4,3], 2), 
               (15, [1,2,3,4,5], 5),
               (15, [5,1,3,5,10,7,4,9,2,8], 2)]
    for tc in tc_list:
        s, lst = tc[:2]
        print("Testing: %d %s, Expect: %d" % (s, lst, tc[2]))
        rtn = test(s, lst)

