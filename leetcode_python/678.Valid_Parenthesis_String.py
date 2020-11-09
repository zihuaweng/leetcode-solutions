#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/valid-parenthesis-string/

class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        hight = 0;
        for c in s:
            if c == '(':
                low += 1
                hight += 1
            elif c == ')':
                if low > 0:
                    low -= 1
                hight -= 1
            else:
                if low > 0:
                    low -= 1
                hight += 1
            if hight < 0:
                return False
        return low == 0