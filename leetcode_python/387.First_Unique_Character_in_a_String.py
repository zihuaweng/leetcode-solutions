#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def firstUniqChar(self, s: str) -> int:
        index = len(s)
        c = collections.Counter(s)
        for val, count in c.items():
            if count == 1:
                index = min(index, s.index(val))

        if not s or index == len(s):
            return -1
        else:
            return index