// https://leetcode.com/problems/friend-circles/

class Solution {
 private:
  vector<int> parent;

 public:
  int findCircleNum(vector<vector<int>>& M) {
    int n = M.size();
    for (int i = 0; i < n; i++) {
      parent.push_back(i);
    }

    for (int i = 0; i < n - 1; i++) {
      for (int j = i + 1; j < n; j++) {
        if (M[i][j] == 1) {
          Union(i, j);
        }
      }
    }

    unordered_set<int> set;
    for (int i = 0; i < n; i++) {
      parent[i] = find(i);
      set.insert(parent[i]);
    }

    return set.size();
  }

  int find(int x) {
    if (x != parent[x]) {
      parent[x] = find(parent[x]);
    }
    return parent[x];
  }

  void Union(int x, int y) {
    int p_x = find(x);
    int p_y = find(y);

    if (p_x != p_y) {
      parent[p_x] = p_y;
    }
  }
};