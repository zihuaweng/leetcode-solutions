#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        final = (1 << n) - 1
        queue = [(i, 1 << i) for i in range(n)]
        seen = set()
        step = 0

        while queue:
            new_q = []
            for node, state in queue:
                if state == final:
                    return step
                for v in graph[node]:
                    if (v, state | 1 << v) not in seen:
                        new_q.append((v, state | 1 << v))
                        seen.add((v, state | 1 << v))

            step += 1
            queue = new_q



