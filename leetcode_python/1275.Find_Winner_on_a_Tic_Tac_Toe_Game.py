# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows = [0] * n
        cols = [0] * n
        diagnoal = 0
        anti_diagnoal = 0
        
        for i, move in enumerate(moves):
            offset = 1 if i & 1 else -1   # 1 is B, -1 is A
            player = 'B' if i & 1 else 'A'
            r, c = move
            rows[r] += offset
            cols[c] += offset
            if r == c:
                diagnoal += offset
            if r+c == 2:
                anti_diagnoal += offset
                
            if abs(rows[r]) == n or abs(cols[c]) == n or abs(diagnoal) == n or abs(anti_diagnoal) == n:
                return player
            
        return 'Draw' if len(moves) == 9 else 'Pending'
            
            
            
                