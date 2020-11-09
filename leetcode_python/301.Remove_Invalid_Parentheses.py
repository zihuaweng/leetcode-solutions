#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def valid(eles):
            stack = []
            for i in eles:
                if stack and i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '(' or i == ')':
                    stack.append(i)

            return len(stack)

        num_to_remove = valid(s)

        res = {s}
        for i in range(num_to_remove):
            temp = set()
            for j in res:
                for k in range(len(j)):
                    if j[k] == '(' or j[k] == ')':
                        temp.add(j[:k] + j[k + 1:])
            res = temp

        ans = [i for i in res if valid(i) == 0]

        return ans





