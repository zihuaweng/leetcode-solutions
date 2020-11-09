#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        S = list(S)
        for i in range(len(S)):
            s = S[i]
            if s == ')':
                if len(stack) > 1:
                    stack.pop()
                else:
                    S[stack.pop()] = ''
                    S[i] = ''
            else:
                stack.append(i)

        return ''.join(S)
