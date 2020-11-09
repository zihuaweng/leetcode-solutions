#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        #         0 1 2 3 4 5 6 7 8
        #         ( a ( b ( c ) d )
        # stack   0
        # invalid

        if not s:
            return ''
        s = list(s)
        stack = []
        for i in range(len(s)):
            cur = s[i]
            if cur == '(':
                stack.append(i)
            elif cur == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''

        for i in stack:
            s[i] = ''

        return ''.join(s)