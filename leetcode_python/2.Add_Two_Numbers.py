# https://leetcode.com/problems/add-two-numbers/
# Time complexity: O(n)
# Space complexity: O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        p = res
        carry = 0
        while l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            val = carry % 10
            carry = carry // 10
            p.next = ListNode(val)
            p = p.next

        if carry:
            p.next = ListNode(carry)
        return res.next


