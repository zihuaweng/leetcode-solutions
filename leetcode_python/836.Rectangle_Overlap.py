#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/rectangle-overlap/

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        l1, b1, r1, u1 = rec1
        l2, b2, r2, u2 = rec2

        width = min(r1, r2) - max(l1, l2)
        height = min(u1, u2) - max(b1, b2)

        return width > 0 and height > 0
