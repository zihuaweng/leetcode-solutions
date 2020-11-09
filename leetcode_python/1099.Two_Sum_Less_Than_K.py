#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/two-sum-less-than-k/
# 双指针

# Time complexity: O(nlogn)
# Space complexity: O(1)


class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        p1 = 0
        p2 = len(A) - 1
        max_sum = float('-inf')
        while p1 < p2:
            if A[p1] + A[p2] >= K:
                p2 -= 1
            else:
                max_sum = max(A[p1] + A[p2], max_sum)
                p1 += 1

        if max_sum == float('-inf'):
            return -1
        else:
            return max_sum
