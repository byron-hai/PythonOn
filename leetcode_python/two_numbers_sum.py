#!/usr/bin/env python3
"""
@ Desc: 
@ Author: Byron
@ Date: 
"""


class Sum:
    @staticmethod
    def two_sum(nums, tar_sum):
        tar_index = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                # print("%d + %d: %d" % (nums[i], nums[j], nums[i] + nums[j]))
                if nums[i] + nums[j] == tar_sum:
                    tar_index.append([i, j])
        return tar_index if tar_index else "Target numbers not found"

    @staticmethod
    def three_sum2zero(nums):
        """
        # way_1, timeout
        tar, tar_sort = [], []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    group = [nums[i], nums[j], nums[k]]
                    if nums[i] + nums[j] + nums[k] == 0 and sorted(group) not in tar_sort:
                        tar.append(group)
                        tar_sort.append(sorted(group))
        return tar
        # way_2, timeout
        tar, tar_sort = [], []
        index = range(len(nums))
        for i in index:
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    group = sorted([nums[i], nums[j], nums[k]])
                    if group not in tar_sort:
                        tar_sort.append(group)
        return [item for item in tar_sort if sum(item) == 0]
        """
        # Way_3, timeout again
        tar, tar_sort = [], []
        index = range(len(nums))
        for num in nums:
            for j in range(i + 1, len(nums)):
                tmp_num = 0 - (nums[i] + nums[j])
                if tmp_num in nums[(j + 1):]:
                    group = sorted([nums[i], nums[j], tmp_num])
                    if group not in tar_sort:
                        tar_sort.append(group)
                        j = nums.index(tmp_num)
        return tar_sort


if __name__ == '__main__':
    sum1 = Sum
    ser_list = [2, 7, 3, 26, 6, 12, 5, 23, 9, 21, 11, 16]
    tar_val = 23
    target = sum1.two_sum(ser_list, tar_val)
    print(target)

    ser2 = [-1, 0, 1, 2, -1, -4]
    # ser2 = [0, 0]
    tar_set = sum1.three_sum2zero(ser2)
    print(tar_set)
