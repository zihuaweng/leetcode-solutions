#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        amount = max(nums)
        dp = [0] * (amount + 1)
        for i in nums:
            dp[i] += i
        d = 0
        n_d = 0
        for i in dp:
            pre = max(d, n_d)
            d = n_d + i
            n_d = pre
        return max(d, n_d)


