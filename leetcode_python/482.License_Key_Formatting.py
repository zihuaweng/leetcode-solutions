#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/license-key-formatting/


# Time complexity: O()
# Space complexity: O()


class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]


    def licenseKeyFormatting2(self, S: str, K: int) -> str:
        stack = []
        temp = ''
        for i in S[::-1]:
            if i != '-':
                temp += i.upper()
                if len(temp) == K:
                    stack.append(temp)
                    temp = ''

        if temp:
            stack.append(temp)

        return '-'.join(stack)[::-1]