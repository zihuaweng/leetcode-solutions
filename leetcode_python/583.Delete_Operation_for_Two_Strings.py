#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/delete-operation-for-two-strings/

# Time complexity: O(n*m)
# Space complexity: O(n*m)


# 第一种dp方法，计算最大公共子序列，然后 m+n-2*p[-1][-1]，总长度减去两倍的公共子序列
# 矩阵第一排第一列都为0
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + (word1[i - 1] == word2[j - 1]))

        return m + n - 2 * dp[-1][-1]

# 第二种dp办法，直接计算需要修改的序列,
# 矩阵第一排第一列为长度，即i+j
class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[-1][-1]


# 空间上的优化，不保存一个二维列表，仅保存前一列的结果。
class Solution3:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [0] * (n + 1)
        for i in range(m + 1):
            temp = [0] * (n + 1)
            for j in range(n + 1):
                if i == 0 or j == 0:
                    temp[j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    temp[j] = dp[j - 1]
                else:
                    temp[j] = min(temp[j - 1], dp[j]) + 1
            dp = temp

        return dp[-1]