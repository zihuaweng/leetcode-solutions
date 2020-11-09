#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = dict()
        tt_set = set()

        for i in range(len(s)):
            ss = s[i]
            tt = t[i]
            if ss not in char_map:
                if tt in tt_set:
                    return False
                else:
                    char_map[ss] = tt
                    tt_set.add(tt)
            else:
                if char_map[ss] != tt:
                    return False

        return True