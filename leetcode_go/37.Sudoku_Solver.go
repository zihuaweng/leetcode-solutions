// https://leetcode.com/problems/sudoku-solver/

func solveSudoku(board [][]byte)  {
    dfs(board, 0, 0)
}

func dfs(board [][]byte, row int, col int) bool {
    if row == 9 {
        return true
    }
    if col == 9 {
        return dfs(board, row+1, 0)
    }
    if board[row][col] != '.' {
        return dfs(board, row, col+1)
    }
    
    for i := byte('1'); i <= '9'; i++ {
        board[row][col] = i
        if isValid(&board, row, col) && dfs(board, row, col+1) {
            return true
        }
    }
    board[row][col] = '.'
    return false
}

func isValid(board *[][]byte, row int, col int) bool {
    for i := 0; i<9; i++ {
        if i != col && (*board)[row][i] == (*board)[row][col] {
            return false
        }
    }
    
    for i := 0; i<9; i++ {
        if i != row && (*board)[i][col] == (*board)[row][col] {
            return false
        }
    }
    
    m := row / 3 * 3
    n := col / 3 * 3
    
    for i := m; i<m+3; i++ {
        for j := n; j<n+3; j++ {
            if i != row && j != col && (*board)[i][j] == (*board)[row][col] {
                return false
            }
        }
    }
    
    return true
}