#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = [[0] * self.n for _ in range(self.m)]
        self.bit = [[0] * (self.n + 1) for _ in range(self.m + 1)]

        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.bit[i][j] += diff
                j += j & -j
            i += i & -i

    def getsum(self, row, col):
        res = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                res += self.bit[i][j]
                j -= j & -j
            i -= i & -i
        return res

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.getsum(row2, col2) - self.getsum(row1 - 1, col2) - self.getsum(row2, col1 - 1) + self.getsum(
            row1 - 1, col1 - 1)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)