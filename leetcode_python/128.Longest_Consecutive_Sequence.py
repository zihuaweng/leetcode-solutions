#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        max_len = 1
        temp = 1
        for i in range(1, len(nums)):
            # print(nums[i])
            if nums[i - 1] != nums[i]:
                if nums[i - 1] == nums[i] - 1:
                    temp += 1
                else:
                    max_len = max(max_len, temp)
                    temp = 1
        max_len = max(max_len, temp)
        return max_len


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        brute force:
        1. sort array.  O(nlogn)
        2. look for num and get the continues nums.  O(n)

        time O(nlogn)
        space O(n) 


        [100, 4, 200, 1, 3, 2]

        - need to find # of increasing consecutive numbers for the current num in O(1):  O(n)
            100: no 101. (1)
            4: no 5 (1)
            1: 234 (4)
            
        - put nums in set so we can find numbers in O(1)

        1. change nums to set(nums)   O(n)
        2. for each num we find all the next consecutive numbers -> #num of consecutive num     length * O(1)
            if num -1 in set, we skip it to avoid duplicated computing
        3. return max(#num of consecutive num)  O(1)

        time: O(n)
        space: O(n)

        """
        if not nums:
            return 0

        res = 0
        nums = set(nums)
        for n in nums:
            temp_res = 1
            if n - 1 not in nums:
                m = n
                while m + 1 in nums:
                    m += 1
                    temp_res += 1
                res = max(temp_res, res)
            # print(n, res)
        return res