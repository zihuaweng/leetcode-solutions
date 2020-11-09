#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n)
# Space complexity: O(1)



# https://leetcode.com/problems/odd-even-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head:
            odd = head
            even = head.next
            right = even
            while even and even.next:
                odd.next = even.next
                odd = odd.next
                even.next = even.next.next
                even = even.next
            odd.next = right
        return head