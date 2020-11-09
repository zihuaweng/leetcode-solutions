# !/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/rotting-oranges/
# https://leetcode.com/problems/rotting-oranges/discuss/238540/python-simple-bfs-solution

# BFS思路，首先记录所有坏橙子（queue）第一分钟先计算现有的边上好橙子，pop完了推入上次所有转化的坏橙子，然后重复

# Time complexity: O(n)  n 为格子数目
# Space complexity: O(n)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        rotten = collections.deque([])
        # 记录下来所有的好橙子和坏橙子，好橙子用来跟踪是不是已经算完了
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2: rotten.append((i, j))
                if grid[i][j] == 1: fresh += 1

        res = 0

        while rotten:
            if fresh == 0:
                return res
            length = len(rotten)
            for _ in range(length):
                x, y = rotten.popleft()
                for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1:
                        grid[i][j] = 2
                        fresh -= 1
                        rotten.append((i, j))
            res += 1

        return res if fresh == 0 else -1

