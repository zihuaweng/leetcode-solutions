#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = collections.Counter(s1)
        length = len(c)
        for i, char in enumerate(s2):
            if char in c:
                c[char] -= 1
                if c[char] == 0:
                    length -= 1

            if i >= len(s1):
                char = s2[i - len(s1)]
                if char in c:
                    if c[char] == 0:
                        length += 1
                    c[char] += 1
            if length == 0:
                return True
        return False

