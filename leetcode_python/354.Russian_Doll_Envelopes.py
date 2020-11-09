#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/russian-doll-envelopes/
# 与300的思路一致
# dp 或者 二分搜索
# 这里dp会超时


class Solution:
    def maxEnvelopes(self, n: List[List[int]]) -> int:
        n = sorted(n, key=lambda x: (x[0], -x[1]))
        dp = []
        length = 0
        for i, e in enumerate(n):
            idx = bisect.bisect_left(dp, e[1])
            if idx == len(dp):
                length += 1
                dp.append(e[1])
            else:
                dp[idx] = e[1]

        return length

#
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        m = len(envelopes)
        if m == 0:
            return 0
        n = sorted(envelopes)
        dp = [1] * m
        for i in range(1, m):
            for j in range(i):
                if n[i][1] > n[j][1] and n[i][0] > n[j][0]:
                    dp[i] = max(dp[i], dp[j]+1)
        # print(m)
        # print(dp)
        return max(dp)