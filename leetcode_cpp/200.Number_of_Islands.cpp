// https://leetcode.com/problems/number-of-islands/

class Solution {
 private:
  int m;
  int n;
  vector<pair<int, int>> dir =
      vector<pair<int, int>>{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

 public:
  int numIslands(vector<vector<char>>& grid) {
    m = grid.size();
    n = grid[0].size();
    int count = 0;

    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (grid[i][j] == '1') {
          count++;
          dfs(grid, i, j);
        }
      }
    }

    return count;
  }

  void dfs(vector<vector<char>>& grid, int row, int col) {
    grid[row][col] = '0';

    for (int i = 0; i < 4; i++) {
      int r = row + dir[i].first;
      int c = col + dir[i].second;

      if (r >= 0 && r < m && c >= 0 && c < n && grid[r][c] == '1') {
        dfs(grid, r, c);
      }
    }
  }
};