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
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        cur = root
        found = False
        stack = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if found:
                return cur
            if cur.val == p.val:
                found = True
            cur = cur.right

        return None


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        _next = None
        while root:
            if root.val > p.val:
                _next = root
                root = root.left
            else:
                root = root.right

        return _next