#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

class Solution:
    def toHex(self, num: int) -> str:
        chars = '0123456789abcdef'
        if num == 0:
            return '0'

        if num < 0:
            num += 1 << 32

        res = ''
        while num != 0:
            res = chars[num & 15] + res
            num >>= 4

        return res

