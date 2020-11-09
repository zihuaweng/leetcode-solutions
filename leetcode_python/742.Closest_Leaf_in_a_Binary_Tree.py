#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        self.graph = collections.defaultdict(set)
        self.start = None
        self.build_graph(root, None, k)
        queue = [self.start]
        seen = set()
        # print(self.graph)
        for q in queue:
            seen.add(q)
            if not q.left and not q.right:
                return q.val
            for n in self.graph[q]:
                if n not in seen:
                    queue.append(n)

    def build_graph(self, node, parent, k):
        if not node:
            return
        if node.val == k:
            self.start = node
        if parent:
            self.graph[parent].add(node)
            self.graph[node].add(parent)
        self.build_graph(node.left, node, k)
        self.build_graph(node.right, node, k)


