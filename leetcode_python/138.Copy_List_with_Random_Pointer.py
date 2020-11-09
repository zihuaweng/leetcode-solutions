#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        self.graph = {}
        return self.dfs(head)

    def dfs(self, node):
        if not node:
            return node
        if node in self.graph:
            return self.graph[node]
        else:
            node_copy = Node(node.val, None, None)
            self.graph[node] = node_copy
            node_copy.next = self.dfs(node.next)
            node_copy.random = self.dfs(node.random)
            return node_copy