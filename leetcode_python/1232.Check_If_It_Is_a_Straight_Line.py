#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        k = None
        for i in range(1, len(coordinates)):
            if k is None:
                k = (coordinates[i][1] - coordinates[i - 1][1]) / (coordinates[i][0] - coordinates[i - 1][0])
            else:
                if (coordinates[i][1] - coordinates[i - 1][1]) / (coordinates[i][0] - coordinates[i - 1][0]) != k:
                    return False
        return True
