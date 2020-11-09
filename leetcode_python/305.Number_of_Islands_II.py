#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/number-of-islands-ii/

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = {}
        rank = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            p_x = find(x)
            p_y = find(y)
            if p_x == p_y:
                return 0

            if rank[p_x] < rank[p_y]:
                p_x, p_y = p_y, p_x
            parent[p_y] = p_x
            rank[p_x] += rank[p_x] == rank[p_y]
            return 1

        counts = []
        count = 0
        for i, j in positions:
            if (i, j) in parent:  # 跳过已经走过的点
                counts.append(count)
                continue
            x = parent[x] = (i, j)
            rank[x] = 0
            count += 1
            for y in (i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1):
                if y in parent:
                    count -= union(x, y)
            counts.append(count)
        return counts