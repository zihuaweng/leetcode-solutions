#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/merge-sorted-array/

# Time complexity: O()
# Space complexity: O()

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = len(nums1) - 1
        m -= 1
        n -= 1
        while n >= 0 and m >= 0:
            if nums1[m] > nums2[n]:
                nums1[idx], nums1[m] = nums1[m], nums1[idx]
                m -= 1
            else:
                nums1[idx] = nums2[n]
                n -= 1
            idx -= 1

        while n >= 0:   # 使用for循环会漏掉
            nums1[n] = nums2[n]
            n -= 1

        return nums1
