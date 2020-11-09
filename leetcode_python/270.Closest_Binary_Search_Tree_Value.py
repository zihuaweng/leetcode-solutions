#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/closest-binary-search-tree-value/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, node: TreeNode, target: float) -> int:
        if not node:
            return None
        res = node.val
        while node:
            if node.val == target:
                return node.val

            if abs(node.val - target) < abs(res - target):
                res = node.val

            if node.val < target:
                node = node.right
            else:
                node = node.left

        return res
