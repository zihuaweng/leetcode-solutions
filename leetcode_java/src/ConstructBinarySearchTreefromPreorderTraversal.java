// https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

 // O(n)

class Solution {
    int i = 0;

    public TreeNode bstFromPreorder(int[] preorder) {
        return helper(preorder, Integer.MAX_VALUE);
    }

    public TreeNode helper(int[] preorder, int bound) {
        if (i >= preorder.length || preorder[i] > bound) {
            return null;
        }
        TreeNode root = new TreeNode(preorder[i++]);
        root.left = helper(preorder, root.val);
        root.right = helper(preorder, bound);
        return root;
    }
}

// Iterative

class Solution {

    public TreeNode bstFromPreorder(int[] preorder) {
        Stack<TreeNode> stack = new Stack<>();
        TreeNode root = new TreeNode(preorder[0]);
        stack.push(root);
        for (int i = 1; i < preorder.length; i++) {
            TreeNode next = new TreeNode(preorder[i]);
            if (preorder[i] < stack.peek().val) {
                stack.peek().left = next;
            } else {
                TreeNode parent = stack.peek();
                while (!stack.isEmpty() && stack.peek().val <= preorder[i]) {
                    parent = stack.pop();
                }
                parent.right = next;
            }
            stack.push(next);
        }
        return root;
    }
}