# https://leetcode.com/problems/unique-paths/
# 典型动态规划问题，现保存一个二维列表，然后每一次结果是左边和上边的加和

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]   # 初始状态设置成1，这样就不用专门设置第一行，第一列，因为他们都是1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                
        return dp[-1][-1]


# recursion
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        
        return self.dfs(m-1, n-1, dp)
    
    def dfs(self, i, j, dp):
        if i < 0 or j < 0:
            return 0
        if i == 0 or j == 0:
            return 1
        if dp[i][j] != 0:
            return dp[i][j]
        dp[i][j] = self.dfs(i-1, j, dp) + self.dfs(i, j-1, dp)
        return dp[i][j]
    