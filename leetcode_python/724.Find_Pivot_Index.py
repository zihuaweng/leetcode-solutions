#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index = -1
        right = sum(nums)
        left = 0
        for i, val in enumerate(nums):
            right -= val
            if left == right:
                return i
            left += val
        return index