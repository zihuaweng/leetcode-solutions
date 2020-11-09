# https://leetcode.com/problems/reverse-linked-list-ii/
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        res = ListNode(0)
        res.next = head
        start = res
        end = n - m
        count = 0
        while count < m - 1:
            start = start.next
            count += 1
        pre = start
        start = start.next
        then = start.next

        for i in range(n - m):
            start.next = then.next
            then.next = pre.next
            pre.next = then
            then = start.next

        return res.next


