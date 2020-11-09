#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O(e*log(e)

# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/
# dijkstra

class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = collections.defaultdict(dict)
        for i, j, n in edges:
            graph[i][j] = n
            graph[j][i] = n

        res = 0
        seen = set()
        heap = [(-M, 0)]
        while heap:
            stops, n = heapq.heappop(heap)
            if n not in seen:
                seen.add(n)
                res += 1
                for i in graph[n]:
                    if graph[n][i] >= 0:
                        if -stops > graph[n][i] and i not in seen:
                            heapq.heappush(heap, (stops + graph[n][i] + 1, i))
                        graph[i][n] -= min(-stops, graph[n][i])
                        res += min(-stops, graph[n][i])
        return res
