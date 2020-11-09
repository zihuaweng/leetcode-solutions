#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O(n)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        end = False
        queue = [root]
        for node in queue:
            if node is None:
                end = True
            else:
                if end:
                    return False
                else:
                    queue.append(node.left)
                    queue.append(node.right)
        return True

# 非常有趣的实现
    def isCompleteTree(self, root):
        bfs = [root]
        i = 0
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i += 1
        return not any(bfs[i:])