# https://leetcode.com/problems/number-of-islands/
# 遍历矩阵，只要遇到“1”就执行helper
# helper里面是每次遇到“1”，就标记成走过了，知道没有“1”为止，这样算是一个小岛

# Time complexity:  O(N*M)
# Space complexity:  O(1)

# 模板
# 先判断条件 if grid[i][j] == '1' || if i not in seen
# 然后dfs 一开始就做操作 grid[i][j] = '2' || seen.add(i)
# 递归的时候判断 边界 + 判断条件

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid, i, j):
        grid[i][j] = '2'
        for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                self.dfs(grid, x, y)
