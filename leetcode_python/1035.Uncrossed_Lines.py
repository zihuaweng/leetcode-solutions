#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/uncrossed-lines/
# 最小公共子序列的变形
# Longest Common Subsequence

# Time complexity: O(N^2)
# Space complexity: O(N^2)

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1] + (A[i - 1] == B[j - 1]))

        return dp[-1][-1]