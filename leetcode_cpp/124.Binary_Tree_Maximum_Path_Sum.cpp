// https://leetcode.com/problems/binary-tree-maximum-path-sum/

class Solution {
 private:
  int res = INT_MIN;

 public:
  int maxPathSum(TreeNode* root) {
    dfs(root);
    return res;
  }

  int dfs(TreeNode* node) {
    if (node == NULL) return 0;

    int left = dfs(node->left);
    int right = dfs(node->right);

    res = max(res, node->val + left + right);
    return max(0, node->val + max(left, right));
  }
};