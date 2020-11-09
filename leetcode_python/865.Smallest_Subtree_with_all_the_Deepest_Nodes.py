# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        return self.helper(root, 0)[0]
        
    def helper(self, node, depth):
        if not node:
            return None, depth
        l_node, l_depth = self.helper(node.left, depth+1)
        r_node, r_depth = self.helper(node.right, depth+1)
        if l_depth == r_depth:
            return node, l_depth
        elif l_depth > r_depth:
            return l_node, l_depth
        else:
            return r_node, r_depth
            
        