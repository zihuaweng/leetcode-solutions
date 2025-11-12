#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n*m)
# Space complexity: O(min(n,m)

# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]

# Reverse recursive
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.get_subsequence(text1, text2, len(text1)-1,len(text2)-1)
    @cache
    def get_subsequence(self, text1, text2, index1, index2):
        if index1 == -1 or index2 == -1:
            return 0

        if text1[index1] == text2[index2]:
            return self.get_subsequence(text1, text2, index1-1, index2-1) + 1
        else:
            return max(self.get_subsequence(text1, text2, index1, index2-1), self.get_subsequence(text1, text2, index1-1, index2))

# Forward recursive
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.get_subsequence(text1, text2, 0,0)
    @cache
    def get_subsequence(self, text1, text2, index1, index2):
        if index1 == len(text1) or index2 == len(text2):
            return 0

        if text1[index1] == text2[index2]:
            return self.get_subsequence(text1, text2, index1+1, index2+1) + 1
        else:
            return max(self.get_subsequence(text1, text2, index1, index2+1), self.get_subsequence(text1, text2, index1+1, index2)
