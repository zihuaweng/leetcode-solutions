#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# Power of 2 means only one bit of n is '1', so use the trick n&(n-1)==0 to judge whether that is the case

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and n&(n-1)==0


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (math.log10(n) / math.log10(2)) % 1 == 0