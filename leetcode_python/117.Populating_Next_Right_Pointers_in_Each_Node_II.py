#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O(1)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        head = None
        pre = None

        while cur:  # 检查每一层的cur
            while cur:  # 检查当前一层的cur
                if cur.left:
                    if pre:
                        pre.next = cur.left
                    else:
                        head = cur.left
                    pre = cur.left

                if cur.right:
                    if pre:
                        pre.next = cur.right
                    else:
                        head = cur.right
                    pre = cur.right

                cur = cur.next

            cur = head
            head = None
            pre = None

        return root

    # 只是一个while，使用dummy node
    def connect2(self, head: 'Node') -> 'Node':
        root = head
        dummy = Node(0, None, None, None)
        pre = dummy
        while root:
            if root.left:
                pre.next = root.left
                pre = pre.next

            if root.right:
                pre.next = root.right
                pre = pre.next

            root = root.next
            if root is None:
                pre = dummy
                root = dummy.next
                dummy.next = None

        return head