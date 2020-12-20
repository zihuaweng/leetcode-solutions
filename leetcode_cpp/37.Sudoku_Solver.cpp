// https://leetcode.com/problems/sudoku-solver/

class Solution {
 public:
  void solveSudoku(vector<vector<char>>& board) { dfs(board, 0, 0); }

  bool dfs(vector<vector<char>>& board, int row, int col) {
    if (row == 9) return true;
    if (col == 9) return dfs(board, row + 1, 0);
    if (board[row][col] != '.') return dfs(board, row, col + 1);

    for (char i = '1'; i <= '9'; i++) {
      board[row][col] = i;
      if (isValid(board, row, col) && dfs(board, row, col + 1)) return true;
    }

    board[row][col] = '.';
    return false;
  }

  bool isValid(vector<vector<char>>& board, int row, int col) {
    for (int i = 0; i < 9; i++) {
      if (i != col && board[row][col] == board[row][i]) return false;
    }

    for (int i = 0; i < 9; i++) {
      if (i != row && board[row][col] == board[i][col]) return false;
    }

    int m = row / 3 * 3;
    int n = col / 3 * 3;

    for (int i = m; i < m + 3; i++) {
      for (int j = n; j < n + 3; j++) {
        if (i != row && j != col && board[i][j] == board[row][col])
          return false;
      }
    }

    return true;
  }
};