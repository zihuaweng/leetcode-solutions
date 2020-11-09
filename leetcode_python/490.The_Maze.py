#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/the-maze/

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:

        # 0 0 1 0 0
        # 0 0 0 0 0
        # 0 0 0 1 0
        # 1 1 0 1 1
        # 0 0 0 0 0
        queue = [start]
        m = len(maze)
        n = len(maze[0])
        for i, j in queue:
            maze[i][j] = 2
            if [i, j] == destination:
                return True
            for _x, _y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_x = i
                new_y = j
                while 0 <= new_x + _x < m and 0 <= new_y + _y < n and maze[new_x + _x][new_y + _y] != 1:
                    new_x += _x
                    new_y += _y
                if maze[new_x][new_y] == 0:
                    queue.append((new_x, new_y))
        return False


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        return self.dfs(maze, start[0], start[1], destination)

    def dfs(self, maze, i, j, destination):
        if maze[i][j] == 2:
            return False
        maze[i][j] = 2
        if [i, j] == destination:
            return True
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            k = i
            l = j
            while 0 <= k + x < len(maze) and 0 <= l + y < len(maze[0]) and maze[k + x][l + y] != 1:
                k = k + x
                l = l + y
            if self.dfs(maze, k, l, destination):
                return True
        return False
