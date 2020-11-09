#https://leetcode.com/problems/out-of-boundary-paths/
class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        """
        1. try different 4 directions
        2. within N: if it is out of bounary: +1
                    
        start: (i, j)
        end: out of bounary + 1
             more than N steps, return
        return count (int)
        
        seen: count of out of boundary in that location
        {(i,j, num of step left): 4}
        
        """
        return self.dfs(m, n, N, i, j, {})
    
    def dfs(self, m, n, N, i, j, seen):
        if i < 0 or i >= m or j < 0 or j >= n:
            return 1
        if N == 0:
            return 0
        if (i, j, N) in seen:
            return seen[(i,j,N)]
        
        count = 0
        for x, y in [(i+1, j), (i-1, j), (i,j-1), (i, j+1)]:
            count += self.dfs(m, n, N-1, x, y, seen)
            
        seen[(i,j,N)] = count % (10**9 + 7)
        return count % (10**9 + 7)
        


class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        """
        dp:
            how many step from boundary to the target slot
            
        we need to think it reversively !
        
        """
        dp = [[0] * n for _ in range(m)]
        for k in range(N):
            temp = [[0] * n for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    a = 1 if x - 1 < 0 else dp[x-1][y]    # if it is bounary, it should be 1
                    b = 1 if x + 1 >= m else dp[x+1][y]
                    c = 1 if y - 1 < 0 else dp[x][y-1]
                    d = 1 if y + 1 >= n else dp[x][y+1]
                    
                    temp[x][y] = (a + b + c + d)  % (10**9 + 7)
            dp = temp
        return dp[i][j]