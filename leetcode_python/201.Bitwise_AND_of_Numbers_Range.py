#!/usr/bin/env python3
# coding: utf-8

#  https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        while m != n:
            m >>= 1
            n >>= 1
            shift += 1
        return m << shift


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while n > m:
            n = n & n-1
        return n&m

