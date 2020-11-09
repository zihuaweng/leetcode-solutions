#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/valid-square/

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        def dist(a, b):
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

        d = collections.defaultdict(int)
        points = [p1, p2, p3, p4]
        for i in range(4):
            for j in range(i + 1, 4):
                d[dist(points[i], points[j])] += 1

        check = d.values()
        if len(d) == 2 and 4 in check and 2 in check:
            return True
        return False
