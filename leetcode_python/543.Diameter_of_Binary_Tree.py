# https://leetcode.com/problems/diameter-of-binary-tree/
# Time complexity: O(n)
# Space complexity: O(n )

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.helper(root)
        return self.diameter

    def helper(self, root):
        if root is None:
            return 0
        l = self.helper(root.left)
        r = self.helper(root.right)
        self.diameter = max(self.diameter, l + r)
        return max(l, r) + 1
