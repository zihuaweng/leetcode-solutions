#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        """
        1. find islands
            dfs, mark visited node to 2
        2. store islands
            represent the island using relative location
            
        """
        m = len(grid)
        n = len(grid[0])
        res = set()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    paths = []
                    self.dfs(grid, i, j, 0, 0, paths)  # TODO
                    res.add(tuple(paths))
                    
        return len(res)
    
    
    def dfs(self, grid, i, j, x, y, paths):
        grid[i][j] = -1
        paths.append((x, y))
        for _x, _y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_i = i+_x
            new_j = j+_y
            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == 1:
                self.dfs(grid, new_i, new_j, x+_x, y+_y, paths)
                
                
                