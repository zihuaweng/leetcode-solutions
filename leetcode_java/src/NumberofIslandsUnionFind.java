// https://leetcode.com/problems/number-of-islands/
// Union find

class Solution {

    private int m;
    private int n;
    private int count = 0;
    private int[] parent;

    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        m = grid.length;
        n = grid[0].length;
        createSet(grid);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '0') continue;
                if (i < m-1 && grid[i+1][j] == '1') {
                    union(i*n + j, (i+1)*n + j);
                }
                if (j < n-1 && grid[i][j+1] == '1') {
                    union(i*n+j, i*n+j+1);
                }
            }
        }
        return count;
    }

    public void createSet(char[][] grid) {
        parent = new int[m*n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                parent[i*n+j] = i*n+j;
                if (grid[i][j] == '1') {
                    count++;
                }
            }
        }
    }

    public int find(int p) {
        if (parent[p] == p) {
            return p;
        }
        parent[p] = find(parent[p]);
        return parent[p];
    }

    public void union(int p1, int p2) {
        int parent1 = find(p1);
        int parent2 = find(p2);
        if (parent1 == parent2) {
            return;
        }
        parent[parent1] = parent2;
        count--;
    }
}