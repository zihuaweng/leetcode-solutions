#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/cousins-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.x_k = 0
        self.x_parent = None
        self.y_parent = None
        self.y_k = 0
        self.dfs(root, x, y, 0, None)
        return self.x_k == self.y_k and self.x_parent != self.y_parent

    def dfs(self, root, x, y, k, pre):
        if not root:
            return
        if root.val == x:
            self.x_parent = pre
            self.x_k = k
        elif root.val == y:
            self.y_parent = pre
            self.y_k = k
        else:
            self.dfs(root.left, x, y, k + 1, root)
            self.dfs(root.right, x, y, k + 1, root)

# bfs
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = collections.deque([root])
        while queue:
            found_x = False
            found_y = False
            for _ in range(len(queue)):
                node = queue.popleft();
                if node.val == x:
                    found_x = True
                if node.val == y:
                    found_y = True
                if node.left and node.right:
                    if node.left.val == x and node.right.val == y:
                        return False
                    if node.right.val == x and node.left.val == y:
                        return False
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if found_x and found_y:
                return True
        return False


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = collections.deque([(root, 0, None)])
        x_parent = None
        y_parent = None
        while queue:
            for _ in range(len(queue)):
                node, k, pre = queue.popleft();
                if node.val == x:
                    x_parent = pre
                if node.val == y:
                    y_parent = pre
                if node.left:
                    queue.append((node.left, k + 1, node))
                if node.right:
                    queue.append((node.right, k + 1, node))
            if x_parent and y_parent:
                if x_parent == y_parent:
                    return False
                else:
                    return True
            if x_parent or y_parent:
                return False




