#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""


class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        while node.parent and node.parent.val < node.val:
            node = node.parent

        return node.parent



