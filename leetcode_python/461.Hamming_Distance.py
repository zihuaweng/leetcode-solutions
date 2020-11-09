#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/hamming-distance/
# 首先异或，求出不同的数字位数，然后计算1的个数

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x ^ y
        res = 0
        while temp:
            res += temp & 1
            temp >>= 1

        return res