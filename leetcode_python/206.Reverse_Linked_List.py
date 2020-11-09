# https://leetcode.com/problems/reverse-linked-list/
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = None
        while head:
            temp = head.next
            head.next = p
            p = head
            head = temp

        return p
