#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


def delNodes(self, root, to_delete):
    to_delete_set = set(to_delete)
    res = []

    def helper(root, is_root):
        if not root:
            return None
        root_deleted = root.val in to_delete_set
        if is_root and not root_deleted:
            res.append(root)
        root.left = helper(root.left, root_deleted)
        root.right = helper(root.right, root_deleted)
        return None if root_deleted else root

    helper(root, True)
    return res


class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        res = []
        check = set(to_delete)
        self.dfs(root, check, res)
        if root.val not in check:
            res.append(root)
        return res

    def dfs(self, root, to_delete, res):
        if not root:
            return None
        root.left = self.dfs(root.left, to_delete, res)
        root.right = self.dfs(root.right, to_delete, res)
        if root.val in to_delete:
            if root.left:
                res.append(root.left)
            if root.right:
                res.append(root.right)
            return None
        return root


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 不用递归完成：

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []
        to_delete_set = set(to_delete)
        stack = [(root, True)]
        while stack:
            cur, is_root = stack.pop()

            root_deleted = cur.val in to_delete_set
            if is_root and not root_deleted:
                res.append(cur)
            if cur.left:
                stack.append((cur.left, root_deleted))
                if cur.left.val in to_delete_set:
                    cur.left = None
            if cur.right:
                stack.append((cur.right, root_deleted))
                if cur.right.val in to_delete_set:
                    cur.right = None

        return res
