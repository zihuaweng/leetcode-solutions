#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        path = set()
        graph = collections.defaultdict(list)
        for u, v in connections:
            path.add((u, v))
            graph[u].append(v)
            graph[v].append(u)

        def dfs(u, parent):
            res = 0
            if (parent, u) in path:
                res += 1
            for v in graph[u]:
                if v != parent:
                    res += dfs(v, u)
            return res

        return dfs(0, -1)
