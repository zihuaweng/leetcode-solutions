#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/pacific-atlantic-water-flow/
# 这道题的意思是说让找到所有点既可以走到左面，上面（pacific）又可以走到右面，下面（atlantic）
# dfs的思路就是，逆向思维，找到从左边,上面（就是第一列&第一排，已经是pacific的点）出发，能到的地方都记录下来.
# 同时右面，下面（就是最后一列，最后一排，已经是Atlantic的点）出发，能到的地方记录下来。
# 综合两个visited矩阵，两个True，证明反过来这个点可以到两个海洋。

# Time complexity: O(MN)
# Space complexity: O(MN)


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        dfs
        treverse the graph twoice, and if the location can be reached by two directions
        that is the result.
        
        start: pac: left up  | atl: right, down
        end: if we can't go to the next
        
        """
        if not matrix:
            return []
        
        res = []
        
        m = len(matrix)
        n = len(matrix[0])
        
        pac_m = [[0] * n for _ in range(m)]        
        atl_m = [[0] * n for _ in range(m)]
        
        for i in range(m):
            self.dfs(matrix, pac_m, i, 0)
            
        for j in range(n):
            self.dfs(matrix, pac_m, 0, j)
        
        for i in range(m):
            self.dfs(matrix, atl_m, i, n-1)
            
        for j in range(n):
            self.dfs(matrix, atl_m, m-1, j)
            
        for i in range(m):
            for j in range(n):
                if pac_m[i][j] == 1 and atl_m[i][j] == 1:
                    res.append([i,j])
                    
        return res
    
    
    def dfs(self, matrix, seen, i, j):
        seen[i][j] = 1
        
        for x, y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
                continue
            if seen[x][y] == 1:
                continue
            if matrix[x][y] < matrix[i][j]:
                continue
            self.dfs(matrix, seen, x, y)
            

# 第二种方法是bfs，使用一个queue去记录可以到达的点，最后同样是合并来给你个能到达的列表的重合返回。

class Solution2:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        # 存放一个四个方位的var方便计算左右上下
        self.direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        m = len(matrix)
        n = len(matrix[0])
        pacific_set = set([(i, 0) for i in range(m)] + [(0, j) for j in range(n)])
        atlantic_set = set([(m - 1, i) for i in range(n)] + [(j, n - 1) for j in range(m)])

        def bfs(reachable_point):
            queue = collections.deque(reachable_point)
            while queue:
                x, y = queue.popleft()
                for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                    nx, ny = x + i, y + j
                    if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and (nx, ny) not in reachable_point and \
                            matrix[nx][ny] >= matrix[x][y]:
                        reachable_point.add((nx, ny))
                        queue.append((nx, ny))
            return reachable_point

        return list(bfs(pacific_set) & bfs(atlantic_set))





