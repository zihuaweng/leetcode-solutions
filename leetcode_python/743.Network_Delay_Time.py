#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O(E log E)

# https://leetcode.com/problems/network-delay-time/
# https://leetcode.com/problems/network-delay-time/discuss/187713/Python-concise-queue-and-heap-solutions
# Dijkstra

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for t in times:
            send, receive, cost = t
            graph[send].append((receive, cost))

        seen = {}
        heap = [(0, K)]
        while heap:
            cost, node = heapq.heappop(heap)
            if node not in seen:      # 这个判断需要在while loop开头，否则cost有可能不是最小值
                seen[node] = cost
                for n, c in graph[node]:
                    heapq.heappush(heap, (cost + c, n))

        if len(seen) == N:
            return max(seen.values())
        else:
            return -1