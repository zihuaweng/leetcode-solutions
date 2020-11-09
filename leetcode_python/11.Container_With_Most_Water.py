#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/container-with-most-water/
# explain why
# https://leetcode.com/problems/container-with-most-water/discuss/200246/Proof-by-formula

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_water = 0
        while start < end:
            max_water = max(max_water, (end - start) * min(height[start], height[end]))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1

        return max_water
