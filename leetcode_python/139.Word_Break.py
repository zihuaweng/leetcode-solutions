#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[-1]


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
          l e e t c o d e
         |      T
                |       T
        """
        word_set = set(wordDict)
        n = len(s)
        dp = [True] + [False] * n
        
        for i in range(n):
            if dp[i]:
                for j in range(i+1, n+1):
                    target = s[i:j]
                    if target in word_set:
                        dp[j] = True
                        
        return dp[-1]

