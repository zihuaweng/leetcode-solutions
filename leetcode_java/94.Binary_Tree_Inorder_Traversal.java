// https://leetcode.com/problems/binary-tree-inorder-traversal/

/**
 * Definition for a binary tree node. public class TreeNode { int val; TreeNode
 * left; TreeNode right; TreeNode() {} TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) { this.val = val; this.left
 * = left; this.right = right; } }
 */
class Solution {
  public List<Integer> inorderTraversal(TreeNode root) {
    Stack<TreeNode> stack = new Stack();
    List<Integer> res = new ArrayList();

    while (root != null || !stack.isEmpty()) {
      while (root != null) {
        stack.push(root);
        root = root.left;
      }
      TreeNode cur = stack.pop();
      res.add(cur.val);
      root = cur.right;
    }

    return res;
  }
}