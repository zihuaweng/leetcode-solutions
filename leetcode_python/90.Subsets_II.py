#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/subsets-ii/
# 和subset1是一样的，差别是有重复的数字
# 解决办法就是在递归中，下一个候选数字中出现是同样的就跳过

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(res, [], 0, nums)
        return res

    def dfs(self, res, temp, start, nums):
        res.append(temp[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:   # 如果遇到重复的跳过
                continue
            self.dfs(res, temp + [nums[i]], i + 1, nums)