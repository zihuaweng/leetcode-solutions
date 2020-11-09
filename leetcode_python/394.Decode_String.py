#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def decodeString(self, s: str) -> str:
        """
        3[a2[c]4[a]]
        
        3 * a2[c]
            a
              2 * c
            
        stack:  ('', 3), 
        num: 
        str: accaaaa
        
        """
        stack = []
        num = 0
        string = ''
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == '[':
                stack.append((string, num))
                string = ''
                num = 0
            elif char == ']':
                prev, _num = stack.pop()
                string = prev + string * _num 
            else:
                string += char
        
        return string