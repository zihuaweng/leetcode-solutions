# https://leetcode.com/problems/largest-bst-subtree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        result = self.helper(root)
        return result[2]
        
    def helper(self, root):
        if not root:
            return (float('inf'), float('-inf'), 0, True)  # min, max, count, is_bst
        min_l, max_l, c_l, is_bst_l = self.helper(root.left)
        min_r, max_r, c_r, is_bst_r = self.helper(root.right)
        
        if not is_bst_l or not is_bst_r or root.val <= max_l or root.val >= min_r:
            return (0, 0, max(c_l, c_r), False)
        
        return (min(min_l, root.val), max(max_r, root.val), c_l+c_r+1, True)


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        result = self.helper(root)
        return result[2]
        
    def helper(self, root):
        if not root:
            return (float('inf'), float('-inf'), 0)
        min_l, max_l, c_l = self.helper(root.left)
        min_r, max_r, c_r = self.helper(root.right)
        
        if root.val <= max_l or root.val >= min_r:
            return (float('-inf'), float('inf'), max(c_l, c_r))
        
        return (min(min_l, root.val), max(max_r, root.val), c_l+c_r+1)