#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """
        We need to compare k+1 size
        Mid is the low pointer, if x-arr[mid] > arr[mid+k]-x, then the first one (mid) is the invalid
        one inside this k+1 range, we pick low = low+1
        otherwise, we pick mid pointer as the high
        """
        low = 0
        hi = len(arr)-k
        while low < hi:
            mid = (low+hi) // 2
            if x-arr[mid] > arr[mid+k]-x:
                low = mid+1
            else:
                hi = mid
                
        return arr[low:low+k]