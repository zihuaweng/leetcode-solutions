// https://leetcode.com/problems/minimum-path-sum/

class Solution {
    public int minPathSum(int[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        int m = grid.length;
        int n = grid[0].length;
        boolean[][] seen = new boolean[m][n];
        int[][] dist = new int[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                dist[i][j] = Integer.MAX_VALUE;
            }
        }
        dist[0][0] = grid[0][0];

        PriorityQueue<int[]> pq = new PriorityQueue<>(m*n, (p1, p2) -> dist[p1[0]][p1[1]] - dist[p2[0]][p2[1]]);

        pq.add(new int[] {0, 0});
        while (!pq.isEmpty()) {
            int[] point = pq.poll();
            int x = point[0];
            int y = point[1];
            int d = dist[x][y];

            if (x == m-1 && y == n-1) {
                return d;
            }

            seen[x][y] = true;

            if (x+1 < m && !seen[x+1][y]) {
                dist[x+1][y] = Math.min(dist[x+1][y], d + grid[x+1][y]);
                pq.add(new int[] {x+1, y});
            }
            if (y+1 < n && !seen[x][y+1]) {
                dist[x][y+1] = Math.min(dist[x][y+1], d + grid[x][y+1]);
                pq.add(new int[] {x, y+1});
            }


        }
        return 0;
    }
}

// https://leetcode.com/problems/minimum-path-sum/
//dp

class Solution {
    public int minPathSum(int[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        int m = grid.length;
        int n = grid[0].length;

        for (int i = 1; i < m; i++) {
            grid[i][0] = grid[i-1][0] + grid[i][0];
        }

        for (int j = 1; j < n; j++) {
            grid[0][j] = grid[0][j-1] + grid[0][j];
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                grid[i][j] = Math.min(grid[i][j-1], grid[i-1][j]) + grid[i][j];
            }
        }
        return grid[m-1][n-1];
    }
}