#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/

class Solution:
    def numOfWays(self, n: int) -> int:
        a_123 = 6
        a_121 = 6
        for i in range(1, n):
            b_123 = a_123*2 + a_121*2
            b_121 = a_123*2 + a_121*3
            a_123 = b_123 % (10**9+7)
            a_121 = b_121 % (10**9+7)
        return  (a_123+a_121) % (10**9+7)