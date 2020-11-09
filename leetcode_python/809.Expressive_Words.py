#!/usr/bin/env python3
# coding: utf-8

#https://leetcode.com/problems/expressive-words/

# Time complexity: O(n)
# Space complexity: O()


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        return sum(self.check(S, W) for W in words)

    def check(self, s, w):
        i = j = 0
        i2 = j2 = 0
        n = len(s)
        m = len(w)

        while i2 < n and j2 < m:
            if s[i] != w[j]:
                return False
            while i2 < n and s[i2] == s[i]:
                i2 += 1
            while j2 < m and w[j2] == w[j]:
                j2 += 1
            if i2 - i != j2 - j and i2 - i < max(3, j2 - j):
                return False
            i = i2
            j = j2

        return i == n and j == m