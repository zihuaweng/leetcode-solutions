#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/cheapest-flights-within-k-stops/
# Dijkstra
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        heap = [(0, 0, src)]
        while heap:
            cost, stops, cur_stop = heapq.heappop(heap)
            if cur_stop == dst:          # 需要在开头判断才是正确的
                return cost
            if stops <= K:
                for v, w in graph[cur_stop]:
                    heapq.heappush(heap, (cost + w, stops + 1, v))

        return -1