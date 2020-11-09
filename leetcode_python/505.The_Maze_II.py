#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        #         0 0 1 0 0
        #         0 0 0 0 0
        #         0 0 0 1 0
        #         1 1 0 1 1
        #         0 0 0 0 0

        if not maze or not maze[0]:
            return None
        m = len(maze)
        n = len(maze[0])
        counts = [[float('inf')] * n for _ in range(m)]
        heap = [(0, start[0], start[1])]
        while heap:
            c, x, y = heapq.heappop(heap)
            if [x, y] == destination:
                return c
            for _x, _y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dist = c
                n_x = x
                n_y = y
                while 0 <= n_x + _x < m and 0 <= n_y + _y < n and maze[n_x + _x][n_y + _y] == 0:
                    n_x += _x
                    n_y += _y
                    dist += 1

                if counts[n_x][n_y] > dist:
                    counts[n_x][n_y] = dist
                    heapq.heappush(heap, (dist, n_x, n_y))

        return -1