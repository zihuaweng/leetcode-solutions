#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/3sum-smaller/
# I think it does not matter and i<j<k<n means one number could not be used more than once.

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        if len(nums) <= 2:
            return 0
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(n - 2):
            if 3 * nums[i] >= target:
                return res
            remain = target - nums[i]
            p1 = i + 1
            p2 = n - 1
            while p1 < p2:
                if nums[p1] + nums[p2] >= remain:
                    p2 -= 1
                else:
                    res += p2 - p1
                    p1 += 1

        return res


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        res = 0
        n = len(nums)
        nums.sort()
        for i in range(n):
            t = target - nums[i]
            j = i + 1
            k = n - 1
            while j < k:
                temp = nums[j] + nums[k]
                if temp >= t:
                    k -= 1
                else:
                    res += k - j
                    j += 1

        return res
