# https://leetcode.com/problems/sort-list/
# 用merge sort的逻辑去直接merge链表
# Time complexity: O(nlogn)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        slow = head
        fast = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.mergeList(left, right)

    def mergeList(self, left, right):
        res = ListNode(0)
        temp = res

        while left is not None and right is not None:
            if left.val > right.val:
                temp.next = right
                right = right.next
            else:
                temp.next = left
                left = left.next
            temp = temp.next

        if left is not None:
            temp.next = left
        if right is not None:
            temp.next = right

        return res.next

