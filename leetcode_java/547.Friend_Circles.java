// https://leetcode.com/problems/friend-circles/

class Solution {
  public int findCircleNum(int[][] M) {
    UnionFind uf = new UnionFind(M.length);

    for (int i = 0; i < M.length - 1; i++) {
      for (int j = i + 1; j < M.length; j++) {
        if (M[i][j] == 1) {
          uf.union(i, j);
        }
      }
    }

    return uf.n;
  }

  class UnionFind {
    int n;
    int[] parent;

    public UnionFind(int n) {
      this.n = n;
      parent = new int[n];
      for (int i = 0; i < n; i++) {
        parent[i] = i;
      }
    }

    public int find(int x) {
      if (x != parent[x]) {
        parent[x] = find(parent[x]);
      }
      return parent[x];
    }

    public void union(int x, int y) {
      int p_x = find(x);
      int p_y = find(y);

      if (p_x != p_y) {
        n--;
        parent[p_x] = p_y;
      }
    }
  }
}