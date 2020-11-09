#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/sliding-window-median/

import bisect

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        arr = nums[:k]
        arr.sort()
        mid = k // 2
        if k % 2 == 0:
            res = [(arr[mid] + arr[mid - 1]) / 2]
        else:
            res = [arr[mid]]

        for i in range(k, len(nums)):
            idx = bisect.bisect_left(arr, nums[i-k])    
            arr.pop(idx)
            bisect.insort_left(arr, nums[i])   # insertion sort
            if k % 2 == 0:
                res.append((arr[mid] + arr[mid - 1]) / 2)
            else:
                res.append(arr[mid])

        return res

