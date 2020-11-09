# https://leetcode.com/problems/valid-tic-tac-toe-state/


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        """
        X is the first, so 
            #X == #O or #X = #O+1
            
        when #X == #O, X could not be the winner
        when #X == #O+1, O could not be the winner
        """
        x = 0
        o = 0
        for line in board:
            for char in line:
                if char == 'X': x += 1
                if char == 'O': o += 1
        
        if not (x==o or x==o+1): return False
        if x==o and self.win(board, 'X'): return False
        if x==o+1 and self.win(board, 'O'): return False
        
        return True
    
    def win(self, board, char):
        # rows
        for line in board:
            if line == char*3:
                return True
            
        # cols
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] == char:
                return True
            
        # diagnoal
        if board[0][0] == board[1][1] == board[2][2] == char:
            return True
        
        if board[0][2] == board[1][1] == board[2][0] == char:
            return True
            
        return False