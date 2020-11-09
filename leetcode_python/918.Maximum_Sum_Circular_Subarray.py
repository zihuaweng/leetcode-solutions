#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O(1)


# https://leetcode.com/problems/maximum-sum-circular-subarray/
class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total = 0
        max_sum = ~sys.maxsize
        max_cur = 0
        min_sum = sys.maxsize
        min_cur = 0
        for n in A:
            max_cur = max(max_cur + n, n)
            max_sum = max(max_cur, max_sum)
            min_cur = min(min_cur + n, n)
            min_sum = min(min_cur, min_sum)
            total += n
        return max(max_sum, total-min_sum) if max_sum > 0 else max_sum