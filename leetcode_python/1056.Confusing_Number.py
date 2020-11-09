#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/confusing-number/

class Solution:
    def confusingNumber(self, a: int) -> bool:
        src = a
        sub = {0: 0, 1: 1, 9: 6, 8: 8, 6: 9}
        b = 0
        while a > 0:
            if a % 10 not in sub:
                return False
            b = b * 10 + sub[a % 10]
            a //= 10
        return src != b


class Solution:
    def confusingNumberII(self, n: int) -> int:
        sub = {0: 0, 1: 1, 9: 6, 8: 8, 6: 9}

        def dfs(num, flip_num, digit):
            res = 0
            if num != flip_num:
                res += 1
            for d, val in sub.items():
                if 0 < num * 10 + d <= n:
                    res += dfs(num * 10 + d, val * digit + flip_num, digit * 10)
            return res

        return dfs(0, 0, 1)
