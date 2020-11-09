#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/longest-valid-parentheses/

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        if (: add to stack
        if ): 
            if stack and stack[-1] == (: pop and calculate the max
            else: add to stack
        
        calculate the max:
        ( * * * * ( * *  
        0 1 2 3 4 5 6 7 
        
        * means the string is popped
        so we have
        stack = [0, 5]
        so we already have 5 - 0 - 1= 4 valid parentheses
        
        if we have next string == ), index = 8
        now stack[-1] == (, stack.pop()
        now stack = [0]
        then the valid length will be 8 - 0 = 7
        so:
            if stack: max = max(max, idx - stack[-1])
            else:     max = max(max, idx - (-1))    # when stack is empty
        """
        stack = []
        res = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    
                    offset = stack[-1] if stack else -1
                    res = max(res, i - offset)
                else:
                    stack.append(i)
                    
        return res
        
        