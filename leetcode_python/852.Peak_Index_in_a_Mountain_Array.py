#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        3,[4],5,1
        arr[mid] < arr[mid+1] : left = mid + 1
        
        3,[4],1
        arr[mid] > arr[mid+1] : right = mid
        
        3,[4],4
        not equal number happen in this question
        """
        
        left = 0
        right = len(arr) - 1   # right should be len(arr)-1 cause we need to compare mid and mid+1, otherwise it will have out of range error.
        
        while left < right:
            mid = (left+right) // 2
            
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left