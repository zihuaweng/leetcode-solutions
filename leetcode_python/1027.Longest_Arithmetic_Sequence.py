#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        gap_map = {}
        n = len(A)
        res = 0
        for i in range(n):
            gap_map[i] = {}
            for j in range(i):
                diff = A[i] - A[j]
                if diff in gap_map[j]:
                    gap_map[i][diff] = gap_map[j][diff] + 1
                else:
                    gap_map[i][diff] = 2

                res = max(res, gap_map[i][diff])

        return res
