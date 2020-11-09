#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/ugly-number/

class Solution:
    def isUgly(self, num: int) -> bool:
        #         6
        #         6/2
        #             3/2 (3/5) [3/3 == 1]
        #         6/3
        #             [2/2 == 1]
        #         6/5

        #         14
        #         14/2
        #             7
        #         (14/3)
        #         (14/5)
        #         remain and divide
        if num == 0:
            return False
        return self.dfs(num)

    def dfs(self, num):
        if num == 1:
            return True
        return any(self.dfs(num // i) for i in [2, 3, 5] if num >= i and num % i == 0)

# 另一种写法
    def isUgly(self, num: int) -> bool:
        for p in 2, 3, 5:
            while num % p == 0 < num:
                num /= p
        return num == 1

class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False

        if num == 1:
            return True

        for i in [2, 3, 5]:
            while num % i == 0:
                num //= i

        return num == 1

