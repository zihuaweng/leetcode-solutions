#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = {0: -1}
        s = 0
        l = 0
        for i, num in enumerate(nums):
            s += num
            target = s - k
            if target in d:
                l = max(l, i - d[target])
            if s not in d:
                d[s] = i

        return l
