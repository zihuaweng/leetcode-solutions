#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if not root or arr[0] != root.val:
            return False
        if len(arr) == 1:
            return not root.left and not root.right
        return self.isValidSequence(root.left, arr[1:]) or self.isValidSequence(root.right, arr[1:])

