#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        dfs + backtrack
        start: (0,0)
        end: go to the 10th line, go to the 11th line
        
        """
        self.dfs(board, 0, 0)  # todo
        
    def dfs(self, board, i, j):
        # base case
        if i == 9:
            return True
        if j == 9:
            return self.dfs(board, i+1, 0)
        if board[i][j] != '.':
            return self.dfs(board, i, j+1)
        
        for k in range(1, 10):
            board[i][j] = str(k)
            if not self.is_valid(board, i, j):
                continue
            if self.dfs(board, i, j+1):
                return True
                
        board[i][j] = '.'
        return False
    
    def is_valid(self, board, i, j):
        for row in range(9):
            if row != i and board[row][j] == board[i][j]: return False
            
        for col in range(9):
            if col != j and board[i][col] == board[i][j]: return False
            
        left_corner_i = i // 3 * 3
        left_corner_j = j // 3 * 3
        
        for x in range(3):
            for y in range(3):
                new_x = left_corner_i+x
                new_y = left_corner_j+y
                if new_x != i and new_y != j and board[new_x][new_y] == board[i][j]: return False
                
        return True
            