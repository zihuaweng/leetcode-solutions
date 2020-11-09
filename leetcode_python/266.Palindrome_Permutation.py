#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


# https://leetcode.com/problems/palindrome-permutation/

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = collections.Counter(s)
        match = 0
        for c in counter.values():
            if c & 1 == 1:
                match += 1
            if match > 1:
                return False
        return True