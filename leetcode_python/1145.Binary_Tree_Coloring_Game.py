#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/binary-tree-coloring-game/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.count_l = 0
        self.count_r = 0
        self.node(root, x)
        p = n - (1 + self.count_l + self.count_r)
        return max(p, max(self.count_l, self.count_r)) > n // 2

    def node(self, root, x):
        if not root:
            return 0
        l = self.node(root.left, x)
        r = self.node(root.right, x)
        if root.val == x:
            self.count_l = l
            self.count_r = r
        return 1 + l + r
