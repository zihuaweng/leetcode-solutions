#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O(n)

# https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            start = max(A[i][0], B[j][0])
            end = min(A[i][1], B[j][1])
            if end >= start:
                res.append([start, end])
            if A[i][1] > B[j][1]:
                j += 1
            else:
                i += 1

        return res