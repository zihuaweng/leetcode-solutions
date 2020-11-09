#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def wordPatternMatch(self, pattern: str, string: str) -> bool:
        d = {}
        return self.helper(pattern, string, d)

    def helper(self, pattern, string, d):
        if not pattern:
            if not string:
                return True
            else:
                return False

        p = pattern[0]
        if p in d:
            if string.startswith(d[p]) and self.helper(pattern[1:], string[len(d[p]):], d):
                return True
            else:
                return False
        else:
            for k in range(1, len(string) - len(pattern) + 2):  # +2 the end, "d"-"e" 会出问题如果没有+2
                if string[:k] not in d.values():
                    d[p] = string[:k]
                    if self.helper(pattern[1:], string[k:], d):
                        return True
                    del d[p]

        return False
