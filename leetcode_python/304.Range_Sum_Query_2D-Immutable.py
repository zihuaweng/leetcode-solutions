#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        n = len(matrix)
        m = len(matrix[0])
        self.pre_sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                self.pre_sum[i][j] = matrix[i - 1][j - 1] + self.pre_sum[i - 1][j] + self.pre_sum[i][j - 1] - \
                                     self.pre_sum[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre_sum[row2 + 1][col2 + 1] - self.pre_sum[row2 + 1][col1] - self.pre_sum[row1][col2 + 1] + \
               self.pre_sum[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)