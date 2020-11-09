#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        n = len(haystack)
        m = len(needle)
        if n < m:
            return -1
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1
