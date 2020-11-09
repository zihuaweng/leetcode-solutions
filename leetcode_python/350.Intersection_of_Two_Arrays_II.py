#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O(n)

# https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = collections.Counter(nums1)
        res = []
        for n in nums2:
            if counts[n] > 0:
                res.append(n)
                counts[n] -= 1
        return res
