#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


# https://leetcode.com/problems/insert-into-a-cyclic-sorted-list/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':

        node = Node(insertVal, head)
        if not head:
            node.next = node
            return node

        pre, cur = head, head.next
        while True:
            if pre.val <= insertVal <= cur.val:
                break
            if pre.val > cur.val and (cur.val > insertVal or pre.val < insertVal):
                break
            if cur == head:
                break
            pre = pre.next
            cur = cur.next

        pre.next = node
        node.next = cur

        return head

