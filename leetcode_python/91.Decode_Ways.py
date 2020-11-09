#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/decode-ways/
# 典型的dp问题，但是需要有一些特殊的判断

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s == "0":
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # 为了后面dp[2]的计算
        dp[1] = 1 if s[0] != "0" else 0
        for i in range(2, len(dp)):
            pre_0 = int(s[i - 1])
            pre_1 = int(s[i - 2:i])
            if pre_0 != 0:
                dp[i] += dp[i - 1]
            if 10 <= pre_1 <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
