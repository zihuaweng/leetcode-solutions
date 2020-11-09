#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/edit-distance/
# 类似leetcode/583.Delete_Operation_for_Two_Strings.py
# 使用的1-d dp存储节省空间
# 与583差别在于这个需要比较左，上，左上所有的点的结果大小，而583只需要比较左，上

# Time complexity: O()
# Space complexity: O()

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [0] * (n + 1)
        for i in range(m + 1):
            temp = [0] * (n + 1)
            for j in range(n + 1):
                if i == 0 or j == 0:
                    temp[j] = i + j
                else:
                    temp[j] = min(dp[j]+1, temp[j - 1]+ 1, dp[j-1]+(word1[i - 1] != word2[j - 1]))
            dp = temp
        return dp[-1]


import Levenshtein

print(Levenshtein.editops("AABACC", "BABCAC"))
