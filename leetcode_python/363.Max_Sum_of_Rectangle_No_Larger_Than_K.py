#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], K: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        A = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                A[i][j] = matrix[i - 1][j - 1] + A[i][j - 1] + A[i - 1][j] - A[i - 1][j - 1]

        res = float('-inf')
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for k in range(i, m + 1):
                    for l in range(j, n + 1):
                        area = A[k][l] - A[k][j - 1] - A[i - 1][l] + A[i - 1][j - 1]
                        # print(str(area) +'aa')
                        if area <= K:
                            print(area)
                            res = max(area, res)
        # print(A)
        return res


