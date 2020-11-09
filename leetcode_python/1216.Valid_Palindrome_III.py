#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


# dp
# 首先参考longestPalindromeSubseq
# https://leetcode.com/problems/longest-palindromic-subsequence
# 使用dp得到最长的回文序列
# 然后进行判断 + k >= len(s)

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        max_len = self.longestPalindromeSubseq(s)
        return max_len + k >= len(s)

    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][n - 1]