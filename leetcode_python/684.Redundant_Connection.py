#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/redundant-connection/
# union find 模板

# 如果是有向图，如果需要找环，那么参照207，计算出度入度
# 如果是无向图，则用union find： 初始状态，每个点的parent都是自己，遍历过程中，如果有一条边的两个点的parent是一样的，
# 说明这两个点都能链接到该parent，加上这个新的边就会成为一个环
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        print(parent)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            p_x = find(x)
            p_y = find(y)
            if p_x == p_y:
                return False
            parent[p_y] = p_x
            return True

        for i, j in edges:
            if not union(i, j):
                return [i, j]
