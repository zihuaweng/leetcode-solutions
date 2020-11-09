#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:

        # 2*3-4*5
        # (2) *  (3-4*5)  --> 2 * [-17, -5]
        # (2*3) - (4*5)   --> 6 - 20
        # (2*3-4) *5 .    --> [2, -2] * 5

        if input.isdigit():
            return [int(input)]

        res = []
        for i in range(len(input)):
            if input[i] in ['-', '+', '*']:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for j in left:
                    for k in right:
                        res.append(self.helper(j, k, input[i]))
        return res

    def helper(self, m, n, op):
        if op == '+':
            return m + n
        if op == '*':
            return m * n
        if op == '-':
            return m - n