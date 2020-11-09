#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/minimum-area-rectangle/

# Time complexity: O()
# Space complexity: O()

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float('inf')
        cor_x = collections.defaultdict(set)
        cor_y = collections.defaultdict(set)
        for x, y in points:
            cor_x[y].add(x)
            cor_y[x].add(y)

        for x, y in points:
            x_list = cor_x[y]
            y_list = cor_y[x]

            for i in x_list:
                for j in y_list:
                    if i == x or j == y:
                        continue
                    if i in cor_x[j] and j in cor_y[i] and abs(i - x) * abs(j - y) > 0:
                        min_area = min(min_area, abs(i - x) * abs(j - y))
            cor_x[y].remove(x)
            cor_y[x].remove(y)

        return min_area if min_area < float('inf') else 0


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = float('inf')
        cor_y = collections.defaultdict(set)
        for x, y in points:
            cor_y[x].add(y)

        for x1, y1 in points:
            for x2, y2 in points:
                if x1 == x2 or y1 == y2:
                    continue
                if y1 in cor_y[x2] and y2 in cor_y[x1]:
                    min_area = min(min_area, abs(x2 - x1) * abs(y2 - y1))

        return min_area if min_area < float('inf') else 0