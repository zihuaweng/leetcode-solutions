#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/surrounded-regions/

# 思路
# 首先将边界上的'O'及他们的邻居变成'S'，这些是不需要改成'X'的'O'
# 然后吧所有的'O'都改成'X'
# 最后吧'S'改回'O'
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board

        m = len(board)
        n = len(board[0])

        # 首先将边界上的'O'及他们的邻居变成'S'，这些是不需要改成'X'的'O'
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    if board[i][j] == 'O':
                        self.dfs(board, i, j)

        # 然后吧所有的'O'都改成'X'
        # 最后吧'S'改回'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'S':
                    board[i][j] = 'O'

    def dfs(self, board, i, j):
        board[i][j] = 'S'
        for _x, _y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x = i + _x
            y = j + _y
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'O':
                self.dfs(board, x, y)



