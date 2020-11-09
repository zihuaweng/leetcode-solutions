#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        sort_h = sorted(horizontalCuts)
        sort_w = sorted(verticalCuts)
        h_h = max(sort_h[0], h - sort_h[-1])
        h_w = max(sort_w[0], w - sort_w[-1])
        for i in range(1, len(sort_h)):
            h_h = max(h_h, sort_h[i] - sort_h[i - 1])
        for i in range(1, len(sort_w)):
            h_w = max(h_w, sort_w[i] - sort_w[i - 1])
        return (h_h * h_w) % (10 ** 9 + 7)
