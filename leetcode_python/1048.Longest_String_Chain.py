#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/longest-string-chain/

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        dp = {}
        for w in words:
            res = 0
            for i in range(len(w)):
                res = max(res, dp.get(w[:i] + w[i + 1:], 0) + 1)
            dp[w] = res

        return max(dp.values())
