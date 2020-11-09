#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        res = '/'
        path = path.split('/')
        if not path:
            return res

        stack = []
        for i in path:
            if i == '.' or i == '':
                continue
            elif i == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(i)

        return res + '/'.join(stack)