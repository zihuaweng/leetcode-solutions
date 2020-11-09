# https://leetcode.com/problems/delete-node-in-a-linked-list/
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node, n):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.val != n:
            node = node.next
        node.val = node.next.val
        node.next = node.next.next
        return
