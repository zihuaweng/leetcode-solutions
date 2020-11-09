#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n^2)
# Space complexity: O(n^2)

# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        """
        xx i xx j
        
        dp[i][j] :  longest palindromic subsequence's length in s[i:j+1]
        if s[i] == s[j]:
            xx i xx j
               [i xx j] only need to check if xx is palindromic
            dp[i][j] = dp[i+1][j-1] + 2
            
        else:
            xx i xx j
            [xx j] or [i xx] could be palindromic subsequence
            
            dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        """
        n = len(s)
        
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
        
        for l in range(2, n+1):   # length
            for i in range(n-l+1):
                j = i + l - 1
                if s[i] == s[j]:
                    # 如果两个数相邻，eg: i = 2, j = 3, dp[i+1][j-1] -> dp[3][2], 没有意义，
                    # 所以我们应该初始化为0，单独对长度为1 的dp赋值 dp[i][i] = 1
                    dp[i][j] = dp[i+1][j-1]+2   
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]) 
                    
                # print(i, j, dp[i][j])
        
        return dp[0][n-1]
        
        