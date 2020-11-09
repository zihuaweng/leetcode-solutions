#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/valid-palindrome-ii/


# Time complexity: O(n)
# Space complexity: O()


class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                left = s[i + 1:j + 1]
                right = s[i:j]
                return left == left[::-1] or right == right[::-1]
            i += 1
            j -= 1
        return True
