# https://leetcode.com/problems/minimum-path-sum/
# 典型递归计算
# 一开始先把第一行和第一列给填完是比较快的方式
# 如果每层去判断是不是小于零有点浪费时间

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
            
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
            
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                
        return grid[-1][-1]
        