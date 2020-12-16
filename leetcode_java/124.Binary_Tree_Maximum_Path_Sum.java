// https://leetcode.com/problems/binary-tree-maximum-path-sum/

class Solution {
  private int max = Integer.MIN_VALUE;

  public int maxPathSum(TreeNode root) {
    dfs(root);
    return max;
  }

  private int dfs(TreeNode root) {
    if (root == null) {
      return 0;
    }

    int left = dfs(root.left);
    int right = dfs(root.right);

    max = Math.max(max, root.val + left + right);
    int cur = Math.max(0, root.val + Math.max(left, right));

    return cur;
  }
}