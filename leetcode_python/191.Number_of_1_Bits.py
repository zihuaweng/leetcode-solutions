#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:
            if n & 1:
                ans += 1
            n >>= 1

        return ans


# Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111. n & (n - 1) will be XXXXXX0000 which is just cancel the last 1
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n != 0:
            n &= n - 1
            ans += 1

        return ans
