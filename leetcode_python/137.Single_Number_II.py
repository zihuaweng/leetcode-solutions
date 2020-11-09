#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for i in range(32):
            _sum = 0
            for n in nums:
                if n >> i & 1 == 1:
                    _sum += 1
            _sum %= 3
            res |= _sum << i
        if res >= 1 << 31:
            return res - (1 << 32)
        else:
            return res



# https://medium.com/@lenchen/leetcode-137-single-number-ii-31af98b0f462
# https://leetcode.com/problems/single-number-ii/discuss/43296/An-General-Way-to-Handle-All-this-sort-of-questions.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = two = 0
        for n in nums:
            temp = (~two & one & n) | (two & ~one & ~n)
            one = (~two & ~one & n) | (~two & one & ~n)
            two = temp
        return one | two


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # approach: by drawing truth table for 00 -> 01 -> 10 -> 00
        #           l' = ~h & (l ^ i)
        #           h' = ~l' & (h ^ i)

        low_bits = high_bits = 0
        for num in nums:
            low_bits = ~high_bits & (low_bits ^ num)
            high_bits = ~low_bits & (high_bits ^ num)
        return low_bits
