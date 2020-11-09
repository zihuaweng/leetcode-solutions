#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/dungeon-game/
# dp 问题
# 这里应该需要有一个表格代表initialhealth，但是可以直接覆盖dungeon来保存值
# subproblem: dungeon[i][j]如果可以到最后公主的格子，dungeon[i][j]需要多少原始能量
# guess: dungeon[i][j]最少需要多少才能到right，down任意一条
# recurrence： dungeon[i][j] = max(1, min(dungeon[i + 1][j], dungeon[i][j + 1]) - dungeon[i][j])
# topological order： right bottom to left upper conner

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 0

        m = len(dungeon)
        n = len(dungeon[0])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    dungeon[i][j] = max(1, 1 - dungeon[i][j])
                elif i == m - 1:
                    dungeon[i][j] = max(1, dungeon[i][j + 1] - dungeon[i][j])
                elif j == n - 1:
                    dungeon[i][j] = max(1, dungeon[i + 1][j] - dungeon[i][j])
                else:
                    dungeon[i][j] = max(1, min(dungeon[i + 1][j], dungeon[i][j + 1]) - dungeon[i][j])

        return dungeon[0][0]