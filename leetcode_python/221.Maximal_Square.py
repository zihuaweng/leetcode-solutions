#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/maximal-square/

# dp

class Solution:
    def maximalSquare(self, A: List[List[str]]) -> int:
        if not A:
            return 0
        m = len(A)
        n = len(A[0])
        max_area = 0

        for i in range(m):
            for j in range(n):
                A[i][j] = int(A[i][j])
                if A[i][j] == 1 and i and j:
                    A[i][j] = min([A[i - 1][j], A[i][j - 1], A[i - 1][j - 1]]) + 1
                max_area = max(max_area, A[i][j])

        return max_area * max_area