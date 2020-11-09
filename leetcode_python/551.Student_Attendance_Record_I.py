#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def checkRecord(self, s: str) -> bool:
        # return s.count('A') < 2 and 'LLL' not in s
        return not re.search('A.*A|LLL', s)