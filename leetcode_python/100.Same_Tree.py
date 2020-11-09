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
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if p and q and p.val == q.val:
                stack.append((p.left, q.left))
                stack.append((p.right, q.right))
            elif not p and not q:
                continue
            else:
                return False

        return True
