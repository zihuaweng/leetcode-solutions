#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/arithmetic-slices/
# 使用dp来解决

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:

        #         opt = [0,0]
        #         i = 2

        #         1,  1,  1,   1，  1,   1,   3， 5, 7
        #         0   0   1   1+2  3+3  6+4
        #       i         2    3    4   5    1  1   2
        if not A:
            return 0
        dp = [0] * len(A)
        c = 1
        for i in range(2, len(A)):
            if A[i - 1] - A[i - 2] == A[i] - A[i - 1]:
                dp[i] = dp[i - 1] + c
                c += 1
            else:
                dp[i] = dp[i - 1]
                c = 1
        # print(dpc)
        return dp[-1]






