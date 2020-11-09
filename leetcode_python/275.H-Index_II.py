#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/h-index-ii/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        i = 0
        j = len(citations)
        while i < j:
            mid = (i + j) // 2
            if citations[mid] < len(citations) - mid:
                i = mid + 1
            else:
                j = mid

        return len(citations) - i