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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            res = [cur.val] + res
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return res