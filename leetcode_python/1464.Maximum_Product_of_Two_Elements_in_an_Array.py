#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = float('-inf')
        n = m
        for num in nums:
            if num >= m:
                n = m
                m = num
            elif num > n:
                n = num
        return (m-1)*(n-1)