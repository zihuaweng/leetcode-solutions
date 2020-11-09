class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        res = 0
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, i, j, dp))
                
        return res
    
    # since the next one should be bigger, so we don't need to use seen to keep track of duplicated visit
    def dfs(self, matrix, i, j, dp):
        if dp[i][j] != 0:
            return dp[i][j]
        
        count = 0
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0<=x<len(matrix) and 0<=y<len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                count = max(count, self.dfs(matrix, x,y, dp))
        
        dp[i][j] = count + 1
        return dp[i][j]
