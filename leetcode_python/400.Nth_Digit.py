#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/nth-digit/discuss/88417/4-liner-in-Python-and-complexity-analysis

# Time complexity: O()
# Space complexity: O()

class Solution:
    def findNthDigit(self, n: int) -> int:
        start = 1
        digit = 9
        length = 1
        while n > digit * length:
            n -= digit * length
            length += 1
            digit *= 10
            start *= 10

        target = start + (n - 1) // length
        return int(str(target)[(n - 1) % length])
