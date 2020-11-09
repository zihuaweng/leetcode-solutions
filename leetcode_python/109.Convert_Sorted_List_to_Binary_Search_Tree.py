#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:

        #         [-10,-3,0,5,9]

        #                mid
        #         left         right
        if not head:
            return None

        return self.dfs(head)

    def dfs(self, head):
        if not head:
            return None
        if not head.next:  # 有可能是只有一个点，就直接返回
            return TreeNode(head.val)

        # find mid
        pre = None
        fast = head
        slow = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        node = TreeNode(slow.val)
        node.right = self.dfs(slow.next)
        pre.next = None
        node.left = self.dfs(head)
        return node
