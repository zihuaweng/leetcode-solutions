// https://leetcode.com/problems/number-of-islands/

var dir = [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

func numIslands(grid [][]byte) int {
    m := len(grid)
    n := len(grid[0])
    count := 0
    
    for i:=0;i<m;i++{
        for j:=0;j<n;j++{
            if grid[i][j] == '1' {
                count++
                dfs(&grid, i, j)
            }
        }
    }
    return count
}

func dfs(grid *[][]byte, row int, col int) {
    (*grid)[row][col] = '0'
    m := len(*grid)
    n := len((*grid)[0])
    
    for i:=0;i<4;i++ {
        r := row+dir[i][0]
        c := col+dir[i][1]
        if r >= 0 && r < m && c >= 0 && c < n && (*grid)[r][c] == '1' {
            dfs(grid, r, c)        
        }
    }
}