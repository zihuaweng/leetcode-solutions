#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/binary-tree-paths/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.res = []
        if not root:
            return self.res

        self.dfs(root, '')  # todo
        return self.res

    def dfs(self, node, temp):
        if not node.left and not node.right:
            self.res.append(temp + str(node.val))
            return
        if node.left:
            self.dfs(node.left, temp + str(node.val) + '->')
        if node.right:
            self.dfs(node.right, temp + str(node.val) + '->')
