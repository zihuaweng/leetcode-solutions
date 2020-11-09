#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [4, 5,  6,  7,  0,  1,  2]
        # i          mid > i      j
        #                  i mid<i j
        #                  ij

        # [3,   1,  2]
        #  i . mid     j
        # i

        i = 0
        j = len(nums) - 1
        while i < j:  # if i <=j will loop forever
            mid = (i + j) // 2
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                j = mid

        return nums[i]



