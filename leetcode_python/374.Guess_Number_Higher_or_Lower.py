#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l <= r:  # todo
            mid = (l + r) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                r = mid - 1
            else:
                l = mid + 1

