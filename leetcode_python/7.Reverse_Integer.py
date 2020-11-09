#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        sig = 1 if x >0 else -1
        res = sig * int(str(abs(x))[::-1])
        return res if (1<<31)-1 >= res >= -1<<31 else 0