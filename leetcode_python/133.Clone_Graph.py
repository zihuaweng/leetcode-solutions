#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

# dfs
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        self.graph = dict()
        return self.dfs(node)

    def dfs(self, node):
        if not node:
            return node
        if node in self.graph:
            return self.graph[node]
        else:
            new_node = Node(node.val, [])
            self.graph[node] = new_node  # 必须先生成才能调用下面的递归
            neighbors = []
            for neig in node.neighbors:
                neighbors.append(self.dfs(neig))
            new_node.neighbors = neighbors
            return new_node

# bfs
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        new_node = Node(node.val, [])
        graph = {node: new_node}
        queue = [node]
        for cur in queue:
            for neig in cur.neighbors:
                if neig in graph:
                    graph[cur].neighbors.append(graph[neig])
                else:
                    new_neig_node = Node(neig.val, [])
                    graph[neig] = new_neig_node
                    graph[cur].neighbors.append(new_neig_node)
                    queue.append(neig)

        return new_node


