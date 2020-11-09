#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if not root:
            return []

        res = []
        graph = collections.defaultdict(set)
        self.build_graph(root, None, graph)
        visited = set()
        queue = [target.val]
        while queue:
            if K == 0:
                return queue
            temp = []
            for node in queue:
                for i in graph[node]:
                    if i not in visited:
                        temp.append(i)
                        visited.add(node)
            queue = temp
            K -= 1
        return res

    def build_graph(self, node, parent, graph):
        if not node:
            return
        if parent:
            graph[parent.val].add(node.val)
            graph[node.val].add(parent.val)
        self.build_graph(node.left, node, graph)
        self.build_graph(node.right, node, graph)


