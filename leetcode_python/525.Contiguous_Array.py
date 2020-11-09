#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/contiguous-array/

# Time complexity: O(n)
# Space complexity: O(k)

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        s = 0
        l = 0
        for i, num in enumerate(nums):
            if num == 0:
                s -= 1
            if num == 1:
                s += 1
            if s in d:
                l = max(l, i - d[s])
            else:
                d[s] = i

        return l