#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        dommy = Node(0, None, None)
        self.pre = dommy
        self.helper(root)
        self.pre.right = dommy.right
        dommy.right.left = self.pre
        return dommy.right

    def helper(self, cur):
        if cur is None:
            return
        self.helper(cur.left)
        self.pre.right = cur
        cur.left = self.pre
        self.pre = cur
        self.helper(cur.right)


"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""

# in

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        dommy = Node(0, None, None)
        pre = dommy
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            pre.right = node
            node.left = pre
            pre = node
            node = node.right
        pre.right = dommy.right
        dommy.right.left = pre
        return dommy.right
