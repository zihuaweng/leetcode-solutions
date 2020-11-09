#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        p1 = 0
        pre = 0
        min_len = len(nums) + 1
        for i, val in enumerate(nums):
            pre += val

            while pre >= s:
                min_len = min(min_len, i - p1 + 1)
                pre -= nums[p1]
                p1 += 1

        return min_len if min_len <= len(nums) else 0