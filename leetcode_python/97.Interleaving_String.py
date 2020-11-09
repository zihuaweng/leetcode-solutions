#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        stack = [(0, 0)]
        seen = set((0, 0))
        while stack:
            print(stack)
            p1, p2 = stack.pop()
            if p1 + p2 == len(s3) and p1 == len(s1) and p2 == len(s2):
                return True
            if p1 + 1 <= len(s1) and s1[p1] == s3[p1 + p2] and (p1 + 1, p2) not in seen:
                stack.append((p1 + 1, p2))
                seen.add((p1 + 1, p2))
            if p2 + 1 <= len(s2) and s2[p2] == s3[p1 + p2] and (p1, p2 + 1) not in seen:
                stack.append((p1, p2 + 1))
                seen.add((p1, p2 + 1))
        return False

# dp做法
# https://www.youtube.com/watch?v=HmAF9xeS_2I
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1 + l2 != l3:
            return False

        dp = [[False] * (l1 + 1) for i in range(l2 + 1)]
        dp[0][0] = True

        for i in range(1, l1 + 1):
            if s1[i - 1] == s3[i - 1]:
                dp[0][i] = dp[0][i - 1]

        for i in range(1, l2 + 1):
            if s2[i - 1] == s3[i - 1]:
                dp[i][0] = dp[i - 1][0]

        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                if s1[j - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i][j - 1]
                if s2[i - 1] == s3[i + j - 1]:
                    dp[i][j] |= dp[i - 1][j]

        return dp[l2][l1]


