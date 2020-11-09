#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = ''
        while i >= 0 or j >= 0:
            _sum = carry
            if i >= 0:
                _sum += ord(num1[i]) - ord('0')
            if j >= 0:
                _sum += ord(num2[j]) - ord('0')

            res = str(_sum % 10) + res
            carry = _sum // 10
            i -= 1
            j -= 1

        if carry:
            res = str(carry) + res
        return res
