#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/palindromic-substrings/

class Solution:
    def countSubstrings(self, s: str) -> int:
        #        a b c
        #      a 1 0 0
        #      b 0 1 0
        #      c 0 0 1

        #        a a a
        #     a  1 1 1
        #     a  0 1 1
        #     a  0 0 1

        res = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]):  # axa, 如果长度为3，两边一样的话，中间无论什么都会是对称的
                    dp[i][j] = True
                    res += 1
        # print(dp)
        return res


class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        aabaaca
          i
          
        1. for each i, we find [xxixx] as palind  count_odd = len(xx)
        2. for each i, i+1, we find [xxi,i+1xx] as palind  count_even = len(xx)
        3. return count_odd + count_even
        
        time O(n^2)
        """
        n = len(s)
        count = 0
        for i in range(n):
            # get odd
            l = r = i
            while l >= 0 and r <= n-1 and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
                    
            l = i
            r = i+1
            while l >= 0 and r <= n-1 and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
                
        return count
        
        
