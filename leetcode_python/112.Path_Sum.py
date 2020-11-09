#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        if not root:
            return False

        if not root.right and not root.left and target == root.val:
            return True

        return self.hasPathSum(root.left, target - root.val) or self.hasPathSum(root.right, target - root.val)