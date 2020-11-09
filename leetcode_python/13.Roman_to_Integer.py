#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/roman-to-integer/

# Time complexity: O()
# Space complexity: O()


class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        pre = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}
        res = pre[s[-1]]

        for i in range(len(s) - 2, -1, -1):
            if pre[s[i]] < pre[s[i + 1]]:
                res -= pre[s[i]]
            else:
                res += pre[s[i]]

        return res


