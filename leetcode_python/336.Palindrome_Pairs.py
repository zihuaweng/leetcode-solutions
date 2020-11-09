#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/palindrome-pairs/
# https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        one in the pair should be the part of the other pair
        
        xxxx  yy yyyy
        we want xxxx[::-1] == yyyy and yy itself is a palindrome
        or
        yyyy yy xxxx
        vice versa
        
        so we can put all words in a dict
        find if they are the substring of any other word
        
        
        """
        d = {w : i for i, w in enumerate(words)}
        
        res = []
        for idx, word in enumerate(words):
            for i in range(len(word)+1):
                str1 = word[:i]
                str2 = word[i:]
                # first part should be palindrome, second part (reverse) should be in w
                if str1 == str1[::-1]:
                    back = str2[::-1]
                    if back in d and back != word:
                        res.append([d[str2[::-1]], idx])
                # second part should be palindrome, first part (reverse) should be in w
                if str2 and str2 == str2[::-1]:   # if the last part is empty, it is calculated before 
                    back = str1[::-1]
                    if back in d and back != word: 
                        res.append([idx, d[str1[::-1]]])
            # print(res)
        return res