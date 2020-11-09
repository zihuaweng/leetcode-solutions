#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/game-of-life/
# 这个题目主要在于怎么找到表示修改前和修改后的方式

# Time complexity: O(m*n)
# Space complexity: O(m*n)

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                lives = 0
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if 0 <= k < m and 0 <= l < n:
                            lives += board[k][l] & 1

                # 因为这个board[i][j] 还没有修改，所以 board[i][j]== board[i][j]&1
                # 这里直接减去lives - board[i][j] 就可以了，如果选择(board[i][j]&1)需要带括号，否则答案错误

                if lives == 3 or lives - board[i][j] == 3:
                    board[i][j] += 2

        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1


