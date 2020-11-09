#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

class Solution:
    def minAddToMakeValid(self, S: str) -> int:

        #         ( ) ) ) ( (
        # stack
        # invalid 0   1 2

        if not S:
            return 0

        stack = []
        invalid = 0
        for s in S:
            if s == ')':
                if stack:
                    stack.pop()
                else:
                    invalid += 1
            else:
                stack.append(s)

        return len(stack) + invalid


class Solution:
    def minAddToMakeValid(self, S: str) -> int:

        #         ( ) ) ) ( (
        # stack
        # invalid 0   1 2

        if not S:
            return 0

        stack = []
        for s in S:
            if stack and s == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(s)

        return len(stack)



