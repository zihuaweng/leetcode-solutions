#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/


# Time complexity: O()
# Space complexity: O()

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.res = None
        self.count = 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.dfs(root, k)
        return self.res

    def dfs(self, node, k):
        if not node:
            return
        self.dfs(node.left, k)
        self.count += 1
        if self.count == k:
            self.res = node.val
            return
        self.dfs(node.right, k)


        # 更快

    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
