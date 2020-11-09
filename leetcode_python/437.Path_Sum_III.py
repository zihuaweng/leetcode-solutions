#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/path-sum-iii/

# Time complexity: O(n)
# Space complexity: O(n*n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def dfs(self, node, target):
        if not node:
            return 0
        target -= node.val
        res = 1 if target == 0 else 0
        return res + self.dfs(node.left, target) + self.dfs(node.right, target)

# Time complexity: O(n)
# Space complexity: O(n)
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        """
        Use prefix sum
        """
        if not root:
            return 0
        mapping = {0: 1}
        return self.dfs(root, 0, target, mapping)

    def dfs(self, node, cur_sum, target, mapping):
        if not node:
            return 0
        cur_sum += node.val
        old_sum = cur_sum - target
        res = mapping.get(old_sum, 0)
        mapping[cur_sum] = mapping.get(cur_sum, 0) + 1
        res += self.dfs(node.left, cur_sum, target, mapping) + self.dfs(node.right, cur_sum, target, mapping)
        mapping[cur_sum] -= 1
        return res

