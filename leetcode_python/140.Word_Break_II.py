#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/word-break-ii/
# dfs 解决，每次看开头是否符合，符合递归后面的s[len(word):]

# Time complexity: O(n*k*n)
# Space complexity: O()


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
        pineapplepenapple
        
        pine + func(applepenapple)  
        pineapple + func(penapple)

        applepenapple 
        apple + func(penapple)
        applepen + func(apple)
        
        func(applepenapple)  -> returns [aa, bb]
        
        pine aa 
        pine bb
        
        optimization:
            memerize the prev result
        """
        d = {}  # key: string, value : list
        
        def dfs(s):
            if s in d:
                return d[s]
            
            res = []
            for word in wordDict:
                if s.startswith(word):
                    idx = len(word)
                    if idx == len(s):
                        res.append(word)
                    else:
                        for result in dfs(s[idx:]):   # return a list
                            res.append(word + ' ' + result)
            d[s] = res
            return res
        
        return dfs(s)
        
