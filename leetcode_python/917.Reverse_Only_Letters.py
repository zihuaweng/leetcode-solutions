#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/reverse-only-letters/

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s_list = list(S)
        l = 0
        r = len(S) - 1
        while l < r:
            if not s_list[l].isalpha():
                l += 1
                continue
            if not s_list[r].isalpha():
                r -= 1
                continue
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1

        return ''.join(s_list)
