#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# # https://leetcode.com/problems/missing-element-in-sorted-array/

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        """
        [4,7,9,10]
        
        binary search
        nums[mid] - nums[0] + 1 = # expected num
        if #expected num < k+ mid + 1:
            left = mid + 1
        else:
            right = mid
            
            
        res: nums[0] + lo + k - 1
        
        We use lo + k - 1 as an offset to retrieve the answer, 
        lo is the number of elements which are present and 
        k is the number of elements which are missing. 
        Because both numbers are 1-indexed, we subtract 1
        """
        lo = 0
        hi = len(nums)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] - nums[0] <  mid + k:
                lo = mid + 1
            else:
                hi = mid
        return nums[0] + lo + k - 1