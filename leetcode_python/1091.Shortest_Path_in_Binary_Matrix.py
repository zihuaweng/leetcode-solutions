#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/shortest-path-in-binary-matrix/

# Time complexity: O()
# Space complexity: O()

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        p = [(0, 0, 1)]
        for i, j, d in p:
            if i == n - 1 and j == n - 1:
                return d
            for k, l in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j + 1), (i, j - 1), (i + 1, j), (i + 1, j - 1),
                         (i + 1, j + 1)]:
                if 0 <= k < n and 0 <= l < n and not grid[k][l]:
                    p.append((k, l, d + 1))
                    grid[k][l] = 1
        return -1
