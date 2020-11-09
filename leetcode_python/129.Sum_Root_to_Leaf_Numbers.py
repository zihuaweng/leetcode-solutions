#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)

    def dfs(self, root, cur_sum):
        if not root:
            return 0
        if not root.left and not root.right:
            return cur_sum * 10 + root.val
        return self.dfs(root.left, cur_sum * 10 + root.val) + self.dfs(root.right, cur_sum * 10 + root.val)


