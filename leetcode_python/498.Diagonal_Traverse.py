#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        #      0        1        2
        # 0  （0，0） （0，1）  （0，2）
        # 1  （1，0） （1，1）  （1，2）
        # 2  （2，0） （2，1）  （2，2）

        # i+j odd -> down
        # i+j even -> up

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])
        res = [0] * (m * n)
        i = 0
        j = 0
        for k in range(len(res)):
            # print(i,j,k)
            res[k] = matrix[i][j]
            if ((i + j) & 1) == 1:  # odd down
                # corner case
                if i == m - 1:  # 走到下边   # 这边的顺序很重，需要先判断最大边界
                    j += 1
                elif j == 0:  # 走到左边
                    i += 1
                else:
                    i += 1
                    j -= 1
            else:  # even up
                if j == n - 1:  # 走到右边  # 这边的顺序很重，需要先判断最大边界
                    i += 1
                elif i == 0:  # 走到上面
                    j += 1
                else:
                    i -= 1
                    j += 1
        return res


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:

        #      0        1        2
        # 0  （0，0） （0，1）  （0，2）
        # 1  （1，0） （1，1）  （1，2）
        # 2  （2，0） （2，1）  （2，2）

        # i+j odd -> down
        # i+j even -> up

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        m = len(matrix)
        n = len(matrix[0])
        lst = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                lst[i + j].append(matrix[i][j])

        res = []
        for k in range(m + n):
            if k & 1 == 1:
                res.extend(lst[k])
            else:
                res.extend(lst[k][::-1])
        return res

