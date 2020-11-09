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
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root:
            return [None, None]
        if root.val <= V:
            _left, right = self.splitBST(root.right, V)
            root.right = _left
            left = root
        else:
            left, _right = self.splitBST(root.left, V)
            root.left = _right
            right = root
        # else:  root.val == V
        #     right = root.right
        #     root.right = None
        #     left = root

        return [left, right]

