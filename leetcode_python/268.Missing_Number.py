#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return n*(n+1)//2 - sum(nums)

    def missingNumber2(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            res = res ^ i ^ nums[i]

        return res ^ n

# 二分搜索
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == mid:
                l = mid + 1
            else:
                r = mid

        return r