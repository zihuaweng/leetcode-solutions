#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/


# Time complexity: O(n)
# Space complexity: O(1)

# 删除需要O(n)，所以选择第二种方法
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        p1 = 0
        p2 = 1
        while p2 < len(nums):
            if nums[p1] != nums[p2]:
                p1 += 1
                p2 += 1
            else:
                del nums[p2]

        return len(nums)


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for n in nums:
            if i < 1 or n > nums[i - 1]:
                nums[i] = n
                i += 1

        return i
