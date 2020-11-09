# https://leetcode.com/problems/design-tic-tac-toe/


# In order to get O(1) for move function, we store the rows, cols, diag, anti_diag.
# Player 1 will +1 while player 2 will -1 for each row, col, diag, anti_diag.
# If there is a n in above data, player 1 wins.
# If there is a -n in above data, player 2 wins.
class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.row = [0] * n
        self.col = [0] * n
        self.diag = 0
        self.anti_diag = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        offset = 1 if player == 1 else -1
        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            self.diag += offset
        if row + col == self.n - 1:
            self.anti_diag += offset
        if offset * self.n in [
                self.row[row], self.col[col], self.diag, self.anti_diag
        ]:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)