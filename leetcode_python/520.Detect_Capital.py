#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word[1:] == word[1:].lower() or word == word.upper()