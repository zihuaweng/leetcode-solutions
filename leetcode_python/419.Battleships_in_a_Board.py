#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/battleships-in-a-board/


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        #         X..X
        #         ...X
        #         ...X

        #         1..1
        #         ...0
        #         ...0

        m = len(board)
        n = len(board[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    flag = 1
                    if i > 0 and board[i - 1][j] == 'X': flag = 0
                    if j > 0 and board[i][j - 1] == 'X': flag = 0
                    count += flag
        return count

# 使用dfs

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:

        m = len(board)
        n = len(board[0])
        count = 0

        def dfs(x, y):
            if x >= m or y >= n or board[x][y] == '.':
                return
            board[x][y] = '#'
            dfs(x + 1, y)
            dfs(x, y + 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    count += 1
                    dfs(i, j)

        return count

