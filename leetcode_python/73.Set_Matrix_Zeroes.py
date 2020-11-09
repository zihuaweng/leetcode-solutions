#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(mn)
# Space complexity: O(1)


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        row_zero = col_zero = False
        for i in range(m):  # 找到第一列为0
            if matrix[i][0] == 0:
                col_zero = True
                break
        for i in range(n):  # 找到第一行为0
            if matrix[0][i] == 0:
                row_zero = True
                break

                # 检查所有cell存在0就记录在第一列第一行上
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 更改cell
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 更改第一列
        if col_zero:
            for i in range(m):
                matrix[i][0] = 0

        # 更改第一行
        if row_zero:
            for i in range(n):
                matrix[0][i] = 0



# Time complexity: O(mn)
# Space complexity: O(m+n)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        col_set = set()
        row_set = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)

        for i in range(m):
            for j in range(n):
                if i in row_set or j in col_set:
                    matrix[i][j] = 0
