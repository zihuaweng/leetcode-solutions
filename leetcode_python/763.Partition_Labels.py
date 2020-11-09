#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        right_most = {c: i for i, c in enumerate(S)}

        res = []
        left = right = 0
        for i, c in enumerate(S):
            right = max(right, right_most[c])
            if right == i:
                res.append(right - left + 1)
                left = i + 1
        return res
