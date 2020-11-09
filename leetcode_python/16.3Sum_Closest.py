#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/3sum-closest/
# 和3sum是一个逻辑
# Time complexity: O(N2)
# Space complexity: O(1)

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        res = 0
        nums.sort()
        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            if start == 1 or nums[i] != nums[i - 1]:
                while start < end:
                    cur_sum = nums[start] + nums[end] + nums[i]
                    if cur_sum == target:
                        return target
                    if abs(cur_sum - target) < diff:
                        diff = abs(cur_sum - target)
                        res = cur_sum
                    if cur_sum < target:
                        start += 1
                    else:
                        end -= 1
        return res
