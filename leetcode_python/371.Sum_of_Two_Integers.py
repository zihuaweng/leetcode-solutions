#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/sum-of-two-integers/


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MAX_INT = (1 << 31) - 1
        MIN_INT = 1 << 31
        MASK = 1 << 32

        while b != 0:
            print(a, b)
            carry = (a & b) << 1
            a = (a ^ b) % MASK
            b = carry % MASK

        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)