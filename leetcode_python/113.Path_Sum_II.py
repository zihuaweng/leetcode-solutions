#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, k: int) -> List[List[int]]:
        res = []
        self.dfs(root, k, [], res)
        return res
        
    def dfs(self, root, k, temp, res):
        if not root:
            return
        
        if not root.left and not root.right and root.val == k:
            res.append(temp + [root.val])
            return
        
        self.dfs(root.left, k-root.val, temp+[root.val], res)
        self.dfs(root.right, k-root.val, temp+[root.val], res)
    