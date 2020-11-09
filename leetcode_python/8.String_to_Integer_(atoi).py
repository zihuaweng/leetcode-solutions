#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:

        s = list(s.strip())
        if not s:
            return 0
        sig = 1
        base = 0
        idx = 0
        if s[0] in '+-':
            sig = 1 if s[0] == '+' else -1
            idx = 1

        while idx < len(s) and s[idx].isdigit():
            base = base * 10 + ord(s[idx]) - ord('0')
            idx += 1

        return max(-1 << 31, min((1 << 31) - 1, base * sig))