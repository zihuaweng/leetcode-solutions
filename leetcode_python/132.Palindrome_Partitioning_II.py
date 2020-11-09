# https://leetcode.com/problems/palindrome-partitioning-ii/


class Solution:
    def minCut(self, s: str) -> int:
        """
        dp[i] : min count of palindromes partitioning of s[:i+1]
        
        xxxxxx[j xxx ]i
        if s[j:i+1] is palindrome:
            dp[i] = min(dp[i], dp[j]+1)
            
        """
        n = len(s) 
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        
        for i in range(n+1):
            for j in range(i):
                if s[j:i] == s[j:i][::-1]:
                    dp[i] = min(dp[i], dp[j]+1)
                # print(i, j, dp[j], dp[i])
        
        return dp[n]-1    # dp is the count of palindrome, so the cutting should -1