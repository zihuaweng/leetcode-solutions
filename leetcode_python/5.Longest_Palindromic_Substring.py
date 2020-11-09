#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        #         a  b  a
        #         |(检查左右是否相等)
        #            |
        #               |

        #         a b b a
        #         |(检查左右是否相等)
        #           |
        #             |
        #               |
        res = ''
        for i in range(len(s)):
            #           检查奇数情况 aba,         检查偶数情况 abba
            res = max(self.helper(s, i, i), self.helper(s, i, i + 1), res, key=len)
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return (l+1, r-1)



class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        expand out from the middle
        
             a b a
        odd  1 3 1
        even 0 0 0
        
             a b b a
        odd  1 1 1 1
        even 0 4 0 0
        
        time O(n^2)
        space O(1)
        """
        
        def longest_length(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            l += 1
            r -= 1
            return r-l+1, l, r 
        
        length = len(s)
        left_index = 0
        right_index = -1
        
        for i in range(length):
            # odd
            odd_length, odd_l, odd_r = longest_length(s, i, i)
            if odd_length > right_index - left_index + 1:
                left_index = odd_l
                right_index = odd_r
                
            # even
            even_length, even_l, even_r = longest_length(s, i, i+1)
            if even_length > right_index - left_index + 1:
                left_index = even_l
                right_index = even_r
                
        return s[left_index:right_index+1]
