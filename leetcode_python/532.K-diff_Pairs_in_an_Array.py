#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/k-diff-pairs-in-an-array/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = collections.Counter(nums)
        res = 0
        for n in d:
            if k>0 and n+k in d or k==0 and d[n] > 1:
                res += 1
        return res