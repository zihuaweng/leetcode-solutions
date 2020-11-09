#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        c = collections.Counter(s)
        sorted_c = sorted(c.items(), key=lambda x: x[1], reverse=True)
        return "".join(char * count for char, count in sorted_c)