#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/shortest-palindrome/

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        r = s[::-1]
        for i in range(n+1):
            if s.startswith(r[i:]):
                return r[:i] + s