#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        def dfs(graph, idx, res, temp):
            if idx == len(graph) - 1:
                res.append(temp)
                return
            for node in graph[idx]:
                dfs(graph, node, res, temp + [node])

        res = []
        dfs(graph, 0, res, [0])
        return res

