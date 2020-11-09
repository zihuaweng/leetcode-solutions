#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/wildcard-matching/
# https://www.youtube.com/watch?v=9OnS06RYQiw&t=454s

class Solution:
    def isMatch(self, p: str, s: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        i = 0
        while i < len(s) and s[i] == '*':  # 初始化星号第一列，如果是星号，应该等于上一个值
            dp[i + 1][0] = dp[i][0]
            i += 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                ss = s[i - 1]
                pp = p[j - 1]
                if ss == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif ss == '?' or ss == pp:
                    dp[i][j] = dp[i - 1][j - 1]

        # print(dp)
        return dp[m][n]