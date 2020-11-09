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

# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [root]
        flag = 1
        while queue:
            if flag > 0:
                res.append([i.val for i in queue])
            else:
                res.append([i.val for i in queue][::-1])
            temp = []
            for q in queue:
                if q.left:
                    temp.append(q.left)
                if q.right:
                    temp.append(q.right)
            queue = temp
            flag *= -1
        return res

