#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/binary-tree-maximum-path-sum/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        path sum = max(0, sum(root.left)) + root.val + max(0, sum(root.right))
        
        cur node works as a child node and return
            cur .val + max(0, sum(cur.left), sum(cur.right))


           -10
           / \
          9  20
            /  \
           15   7   


           -10
           / \
          9  42  

        cur_max = 42 | 41
        
        test case &corner case:
            1
            
            
        time O(n)
        space O(1)
        """
        self.max_val = float('-inf')
        self.dfs(root)
        return self.max_val
        
    def dfs(self, root):
        if not root:
            return 0
        
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        cur = root.val + left + right
        self.max_val = max(self.max_val, cur)
        
        return max(0, root.val + max(left, right))


# without global valuable
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = self.dfs(root)
        return res[1]
        
    def dfs(self, root):
        if not root:
            return 0, float('-inf')
        
        left, left_max = self.dfs(root.left)
        right, right_max = self.dfs(root.right)
        
        cur = root.val + left + right
        cur_max = max(left_max, right_max, cur)
        
        return max(0, root.val + max(left, right)), cur_max