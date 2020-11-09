#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/search-a-2d-matrix/submissions/

# Time complexity: O(log(mn))
# Space complexity: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows, cols = len(matrix), len(matrix[0])
        r = 0
        c = cols - 1
        while r < rows and c >= 0:
            if matrix[r][c] > target:
                c -= 1
            elif matrix[r][c] < target:
                r += 1
            else:
                return True
        return False

    # 因为是一个排好序的矩阵，转换后就是一个排序的列表，可以使用二分搜索
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        rows, cols = len(matrix), len(matrix[0])
        start = 0
        end = rows * cols - 1
        while start <= end:
            mid = (start + end) // 2
            num = matrix[mid // cols][mid % cols]
            if num > target:
                end = mid - 1
            elif num < target:
                start = mid + 1
            else:
                return True
        return False

