#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        count = [0] * (N + 1)
        for u, v in trust:
            count[u] -= 1
            count[v] += 1

        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1