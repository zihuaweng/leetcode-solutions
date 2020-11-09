#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        find the bondary
        where:
        x < 0
        x >= m
        y < 0
        y >= n
        grid[x][y] == 0
        
        each bondary += 1
        """
        m = len(grid)
        n = len(grid[0])
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for x, y in [(i, j-1),(i, j+1),(i-1, j), (i+1, j)]:
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0:
                            count += 1
                    
        return count