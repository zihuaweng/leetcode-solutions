# https://leetcode.com/problems/maximum-profit-in-job-scheduling/

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        """
        
        dp[i] maximum profit you can take using time[:i+1]
        
        |___|_______|
          |_____|
            |___|
              
        pick i : dp[i] = profit[i] + dp[x]   x is the idx where biggest end time < cur start time
        not pick i: dp[i] = dp[i-1]
        
        => max(pick, not pick)
        
        """
        n = len(endTime)
        times = list(zip(endTime, startTime, profit))
        times.sort()
        end_time = [i for i, _, _ in times]
        
        dp = [float('-inf')] * (n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            idx = bisect.bisect_right(end_time, times[i-1][1])  # find the index of right time
            dp[i] = max(dp[i-1], times[i-1][2]+dp[idx])
            
        return dp[-1]
        
        
        