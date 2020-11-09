#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = collections.Counter(s)
        for tt in t:
            if tt not in c:
                return False
            else:
                if c[tt] == 0:
                    return False
                c[tt] -= 1
        return not any(c.values())