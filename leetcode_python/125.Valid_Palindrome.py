#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O(n)

# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        i = 0
        j = len(s) - 1

        while i <= j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1

        return True

