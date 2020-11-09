# https://leetcode.com/problems/symmetric-tree/
# 递归实现，是否左边和右边一样即可

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self.helper(root, root)

    def helper(self, l, r):
        if not l and not r:
            return True
        if not l or not r or l.val != r.val:
            return False
        return self.helper(l.right, r.left) and self.helper(l.left, r.right)
