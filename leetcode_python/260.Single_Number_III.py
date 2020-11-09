#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/single-number-iii/

# The idea is get the XOR of the two distinct numbers
# say the result is 6 which is 110, then location 3 and 2 of these two numbers must be diff, so that they can get 1
# we can group them into two groups. each group must contain one distinct number
# do another XOR in each group can get the result.

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # first get the XOR result of the two distinct numbers
        temp = 0
        for n in nums:
            temp ^= n

        # find the right most 1
        mask = temp & -temp

        res = [0, 0]
        for n in nums:
            if n & mask == 0:  # means this location == 0, we put this in one group, all others in other group.
                res[0] ^= n
            else:
                res[1] ^= n
        return res