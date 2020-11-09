#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/number-of-digit-one/
# https://www.youtube.com/watch?v=uB7DfQul6GU

class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        l = n
        x = 1
        while l > 0:
            a = l % 10
            l = l // 10

            count += l * x
            if a > 1:
                count += x
            elif a == 1:
                count += n % x + 1
            x *= 10
        return count