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

# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/



class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0

        self.max_len = 0
        self.dfs(root, 0, root.val)
        return self.max_len

    def dfs(self, node, count, target):
        if not node:
            return
        if node.val == target:
            count += 1
        else:
            count = 1
        self.max_len = max(self.max_len, count)
        self.dfs(node.left, count, node.val + 1)
        self.dfs(node.right, count, node.val + 1)
