#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i, n in enumerate(nums):
            m = target - n
            if m in seen:
                return [seen[m], i]
            else:
                seen[n] = i


class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, n in enumerate(nums):
            if n in seen:
                return [seen[n], i]
            else:
                seen[target-n] = i