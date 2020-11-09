#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/find-eventual-safe-states/

# Time complexity: O(N)
# Space complexity: O(N)

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        out_degree = [0] * len(graph)
        in_node = collections.defaultdict(list)
        queue = []
        # 首先记录下来所有点的出度，如果0，证明是一个terminal的点
        # 还需要记录每一个点的入点有哪些，只要他们的下一个点的出度为0，这个点可以删除，那么原是出发的点就可以减少一个出度了
        for i in range(len(graph)):
            out_degree[i] = len(graph[i])
            if out_degree[i] == 0:
                queue.append(i)
            for j in graph[i]:
                in_node[j].append(i)

        # 检索所有出度为0的点，如果出度为0，证明是一个terminal的点，同时更新上一个点的出度。
        # 这里queue可以不用pop，直接使用作为结果
        for i in queue:
            for j in in_node[i]:
                out_degree[j] -= 1
                if out_degree[j] == 0:
                    queue.append(j)

        return sorted(queue)