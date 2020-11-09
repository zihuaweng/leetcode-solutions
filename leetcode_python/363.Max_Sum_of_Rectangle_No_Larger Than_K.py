#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

class Solution:
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """

        assert(len(matrix) > 0 and len(matrix[0]) > 0)

        rows = len(matrix)
        cols = len(matrix[0])

        ans = float('-inf')
        for i in range(cols):
            colsum = [0] * rows
            for j in range(i, cols):
                curlist = [0]
                rowsum = 0
                for r in range(rows):
                    # sum up columns in each row from i to j, use prefix sum to speed up
                    colsum[r] += matrix[r][j]
                    # sum up rows up to r
                    rowsum += colsum[r]
                    # find the smallest element larger than rowsum-k if exists
                    idx = bisect.bisect_left(curlist, rowsum - k)
                    # update final answer
                    if idx >= 0 and idx < len(curlist):
                        ans = max(ans, rowsum - curlist[idx])
                    # update the set of cums(or ordered list here)
                    bisect.insort(curlist, rowsum)

        return ans