#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/sparse-matrix-multiplication/
# https://leetcode.com/problems/sparse-matrix-multiplication/discuss/76154/Easiest-JAVA-solution
# https://www.youtube.com/watch?v=bOmAllndo-4
# http://www.cs.cmu.edu/~scandal/cacm/node9.html

class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        row_a, col_a = len(A), len(A[0])
        row_b, col_b = len(B), len(B[0])

        res = [[0 for _ in range(col_b)] for _ in range(row_a)]

        for i in range(row_a):
            for k in range(col_a):
                if A[i][k] != 0:
                    for j in range(col_b):
                        res[i][j] += A[i][k] * B[k][j]
        return res

# brute force
class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m = len(A)
        n = len(B[0])
        l = len(A[0])
        res = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                for k in range(l):
                    res[i][j] += A[i][k] * B[k][j]
                    
        return res