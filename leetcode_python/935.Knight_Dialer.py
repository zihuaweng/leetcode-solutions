#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(10 * N)
# Space complexity: O(N)

# https://leetcode.com/problems/knight-dialer/
# 经典dp问题

class Solution:
    def knightDialer(self, N: int) -> int:
        dp = [1] * 10
        pre_nodes = [[6, 4], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [6, 2], [3, 1], [2, 4]]
        M = 10 ** 9 + 7
        for i in range(1, N):
            temp = [0] * 10
            for idx, nodes in enumerate(pre_nodes):
                for n in nodes:
                    temp[idx] += dp[n]
                    temp[idx] %= M
            dp = temp

        res = 0
        for i in dp:
            res += i
            res %= M
        return res


