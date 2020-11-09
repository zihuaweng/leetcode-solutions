#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/


# similar to 340

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        d = {}
        max_len = 0
        for i, val in enumerate(s):
            if val in d and d[val] >= left:
                left = d[val] + 1
            d[val] = i
            max_len = max(max_len, i - left + 1)
        return max_len