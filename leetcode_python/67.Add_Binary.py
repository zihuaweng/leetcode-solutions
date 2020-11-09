#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = ''
        while i >= 0 or j >= 0:
            _sum = carry
            if i >= 0:
                _sum += int(a[i])
            if j >= 0:
                _sum += int(b[j])
            res = str(_sum & 1) + res
            carry = _sum >> 1
            i -= 1
            j -= 1
        if carry:
            res = str(carry) + res
        return res
