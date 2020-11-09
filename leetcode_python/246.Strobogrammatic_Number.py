#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/strobogrammatic-number/

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if not num:
            return True
        maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}
        i = 0
        j = len(num) - 1
        while i <= j:
            s = num[i]
            e = num[j]
            if (s, e) not in maps:
                return False
            i += 1
            j -= 1

        return True
