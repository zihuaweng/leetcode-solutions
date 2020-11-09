#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.dfs(s, res, [])
        return res

    def dfs(self, s, res, temp_res):
        if not s:
            res.append(temp_res)
            return
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                self.dfs(s[i:], res, temp_res + [s[:i]])

