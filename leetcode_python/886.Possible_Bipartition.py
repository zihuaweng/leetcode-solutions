#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O(n)

# https://leetcode.com/problems/possible-bipartition/

# 思路和代码都和785一致
# 唯一不同就是需要自己构建graph

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        g = {}
        graph = collections.defaultdict(list)

        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        for i in range(1, N + 1):
            if i not in g and not self.dfs(graph, g, i, 1):  # 已经确定好分组的就不需要再走
                return False
        return True

    def dfs(self, graph, g, node, val):
        g[node] = val
        for i in graph[node]:
            if i in g:
                if g[i] == val:
                    return False
            else:
                if not self.dfs(graph, g, i, -val):
                    return False
        return True


