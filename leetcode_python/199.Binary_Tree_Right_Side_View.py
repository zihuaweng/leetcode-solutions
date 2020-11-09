#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/binary-tree-right-side-view/
#

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            length = len(queue)
            res.append(queue[-1].val)
            while length > 0:
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                length -= 1

        return res


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        self.view_right(res, root, 0)
        return res

    def view_right(self, res, node, depth):
        if not node:
            return
        if depth == len(res):
            res.append(node.val)

        self.view_right(res, node.right, depth + 1)
        self.view_right(res, node.left, depth + 1)
