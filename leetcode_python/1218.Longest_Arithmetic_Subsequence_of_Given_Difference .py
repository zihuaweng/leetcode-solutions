#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = 0
        dp = {}
        for i in range(len(arr)):
            dp[arr[i]] = dp.get(arr[i] - difference, 0) + 1
            res = max(dp[arr[i]], res)

        return res