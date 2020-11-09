# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        区间型 dp
        corner case:
            len(arr) < d
            
            
        dp[i][k] : minimum difficulty of job[:i] when spilt into k days
        
        xxxxxx [jxxxxxi]
        
        k days
        
        dp[i][k] = dp[j-1][k-1] + max(job[j:i+1])
        """
        if len(jobDifficulty) < d:
            return -1
        
        n = len(jobDifficulty)
        jobDifficulty = [0] + jobDifficulty   # in case we need to use i-1 below
        dp = [[float('inf')] * (d+1) for _ in range(n+1)]
        
        dp[0][0] = 0
        
        for i in range(1, n+1):
            for k in range(1, d+1):
                if k > i:   # k should be samller than i
                    continue
                max_val = jobDifficulty[i]
                for j in range(i, k-1, -1): 
                    max_val = max(max_val, jobDifficulty[j])
                    dp[i][k] = min(dp[i][k], dp[j-1][k-1] + max_val)
                        
        print(dp)
        return dp[n][d]
        
        