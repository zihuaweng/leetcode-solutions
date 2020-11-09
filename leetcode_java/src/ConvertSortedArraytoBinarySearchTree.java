// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {

    public TreeNode sortedArrayToBST(int[] nums) {
        return createNode(nums, 0, nums.length-1);
    }

    public TreeNode createNode(int[] nums, int left, int right) {
        if (left > right) {
            return null;
        }
        int mid = left + (right - left) / 2;
        TreeNode node = new TreeNode(nums[mid]);
        node.left = createNode(nums, left, mid-1);
        node.right = createNode(nums, mid+1, right);
        return node;
    }
}