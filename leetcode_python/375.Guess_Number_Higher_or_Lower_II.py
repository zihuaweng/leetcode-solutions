#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/guess-number-higher-or-lower-ii/
# https://www.youtube.com/watch?v=VfJPDNG0nYM&t=67s

class Solution:
    def getMoneyAmount(self, n: int) -> int:

        # 1 2 3 4 5
        # 1: 1 + max([0], [2 3 4 5])
        # 2: 2 + max([1], [3 4 5])
        # 3: 3 + max([1 2], [4 5])
        # 4: 4 + max([1 2 3], [5])
        # 5: 5 + max([1 2 3 4], [6])

        # dfs(i, j)
        # for k in range(i, j+1):
        #   k + max(dfs(i, k-1), dfs(k+1, j))
        # 可以dp解决
        # ==> dp[i][j]

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for length in range(2, n + 1):
            for start in range(1, n - length + 2):
                val = float('inf')
                end = start + length - 1
                for k in range(start, end):
                    val = min(val, k + max(dp[start][k - 1], dp[k + 1][end]))
                dp[start][end] = val
        # print(dp)
        return dp[1][n]
