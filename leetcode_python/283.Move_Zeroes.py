#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/move-zeroes/
# 两个指针方法

# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #         1,  3,  0,  0,  12
        #                 |  |     i

        #         nums[i] <-> nums[slow]

        #         slow += 1 (0)
        #         i = 1

        slow = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                nums[i], nums[slow] = nums[slow], nums[i]
                slow += 1

        return nums

