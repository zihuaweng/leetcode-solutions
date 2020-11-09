#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)

        if k:
            stack = stack[:-k]

        return "".join(stack).lstrip("0") or "0"