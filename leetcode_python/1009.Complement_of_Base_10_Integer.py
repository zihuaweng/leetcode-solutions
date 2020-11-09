#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

class Solution:
    def findComplement(self, num: int) -> int:
        x = 1
        while x < num:
            x = (x << 1) + 1
        return x ^ num  # x-num
