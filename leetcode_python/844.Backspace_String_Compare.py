#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/backspace-string-compare/

# Time complexity: O()
# Space complexity: O(1)


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        """
         ab#c  ad#c
         l
            r
        right pointer keep going to the end
        left pointer:
            char == '#':
                left -= 1
            else:
                s[left] = s[right]
                left += 1
        """
        index_l, s = self.get_idx(S)
        index_r, t = self.get_idx(T)
        
        return s[:index_l] == t[:index_r]
    
    def get_idx(self, string):
        string = list(string)
        i = 0
        for j, char in enumerate(string):
            if char != '#':
                string[i] = char
                i += 1
            else:
                i = max(0, i-1)
                
        return i, ''.join(string)
        
            