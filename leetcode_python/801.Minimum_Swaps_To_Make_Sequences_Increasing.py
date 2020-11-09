#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
# https://www.youtube.com/watch?v=__yxFFRQAl8

class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        swap = [float('inf')] * n
        keep = [float('inf')] * n

        keep[0] = 0
        swap[0] = 1

        for i in range(1, n):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                keep[i] = keep[i - 1]
                swap[i] = swap[i - 1] + 1

            if A[i] > B[i - 1] and B[i] > A[i - 1]:
                keep[i] = min(keep[i], swap[i - 1])
                swap[i] = min(swap[i], keep[i - 1] + 1)

        return min(swap[-1], keep[-1])
