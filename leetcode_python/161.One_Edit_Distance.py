#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/one-edit-distance/

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if m < n:
            return self.isOneEditDistance(t, s)

        if m - n > 1:
            return False
        elif m == n:
            diff = 0
            for i in range(m):
                if s[i] != t[i]:
                    diff += 1
            return diff == 1
        else:
            for i in range(n):
                if s[i] != t[i]:
                    return s[i + 1:] == t[i:]
            return True
