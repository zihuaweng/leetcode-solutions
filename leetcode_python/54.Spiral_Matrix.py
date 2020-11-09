#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(mn)
# Space complexity: O()

# 简单方法，速度慢
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        return [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


# 更快的方法
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9,10,11,12]
        ]
        
        4 pointer

        - row = 0, col = 0-cols-1
        - row = 1-rows-1, col = cols-1
        - row = rows-1, col = cols-2, 0
        - row = rows-2-1, col = 0

        at the end it could be :
        a horizontal matrix
        xxxxxxxx
        a vertical matrix
        x
        x
        x
        x
        so, we alway need to go left to right, up to down, so the last two for loop and skip if we get all the results.

        """
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        up, down, left, right = 0, m-1, 0, n-1
        res = []
        while len(res) < m*n:
            res.extend([matrix[up][i] for i in range(left, right+1)])
            up += 1
            res.extend([matrix[i][right] for i in range(up, down+1)])
            right -= 1
            if len(res) < m*n:   # if there is no num left to add, skip it
                res.extend([matrix[down][i] for i in range(right, left-1, -1)])
                down -= 1
            if len(res) < m*n:   # ditto
                res.extend([matrix[i][left] for i in range(down, up-1, -1)])
                left += 1
        return res