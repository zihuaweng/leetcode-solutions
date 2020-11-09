#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 最优解
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        """
        abcdebdde

         b de
          bde


        brute force
        time O(n*n)
        n: length of S
        k: length of T
        
        
        optimize:
        fffffffffffffffffffffffffffffffffffffffabc
        fabc
        
        fffffffffffffffffffffffffffffffffffffffabc
                                              fabc  (we want to start from the last f not the seconde f)
        match the end of T, then we move the left pointer to the cloest left, so we don't need to run duplicated times.
        
        corner case:
            S = '' T=''
            len(s) < len(T)

        time O(nm)
        space O(1)
        """
        i = 0
        left = 0
        right = 0
        length = float('inf')
        res = ""
        j = 0
        while i < len(S): 
            if S[i] == T[j]:
                if j == len(T) - 1:
                    # check feasibility from left to right of T
                    right = i+1
                    # check optimization from right to left of T
                    while j > 0:
                        while S[i-1] != T[j-1]:
                            i -= 1
                        i -=1
                        j -= 1
                    if right - i < length:
                        length = right - i
                        res = S[i:right]
                else:
                    j+=1
            
            i += 1
        
        return res


def minWindow(self, S: str, T: str) -> str:
        """
        abcdebdde

         b de
          bde


        brute force
        time O(n*n)
        n: length of S
        k: length of T
        
        
        optimize:
        fffffffffffffffffffffffffffffffffffffffabc
        fabc
        
        fffffffffffffffffffffffffffffffffffffffabc
                                              fabc  (we want to start from the last f not the seconde f)
        match the end of T, then we move the left pointer to the cloest left, so we don't need to run duplicated times.
        
        corner case:
            S = '' T=''
            len(s) < len(T)
            
        dp:
        abcdebdde
        012345678
      b  1   5
      d    1  5
      e     1    5
      
         11115555
      
        res = 4-1+1 = 4
        
        1. for each char in T, we check if its previous char appear in S
        2. calculate the min_length of all substring

        time O(nm)
        space O(n)
        """
        l_s = len(S)
        l_t = len(T)
        dp = [[-1] * l_s for _ in range(l_t)]
        # set up the first row
        for i in range(l_s):
            if S[i] == T[0]:
                dp[0][i] = i
                
        # find the left and right index
        for i in range(1, l_t):
            idx = -1
            for j in range(l_s):
                if S[j] == T[i] and idx != -1:
                    dp[i][j] = idx
                if dp[i-1][j] != -1:
                    idx = dp[i-1][j]

        # find the min_res
        length = float('inf')
        res = ''
        for i in range(l_s):
            idx = dp[l_t-1][i]
            if idx != -1 and i - idx + 1 < length:
                res = S[idx:i+1]
                length = i-idx+1
                
        return res