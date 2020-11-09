#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(mn)
# Space complexity: O()

import collections

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        a = list()
        b = list()
        d = collections.defaultdict(int)

        rows = len(A)
        cols = len(A[0])

        for i in range(rows):
            for j in range(cols):
                if A[i][j] == 1:
                    a.append((i, j))
                if B[i][j] == 1:
                    b.append((i, j))

        res = 0
        for x, y in a:
            for i, j in b:
                d[(x - i, y - j)] += 1
                res = max(res, d[(x - i, y - j)])
        return res