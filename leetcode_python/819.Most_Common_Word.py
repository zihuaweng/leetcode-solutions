#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/most-common-word/

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        words = re.findall('\w+', paragraph.lower())
        c = collections.Counter([i for i in words if i not in banned])
        return c.most_common(1)[0][0]