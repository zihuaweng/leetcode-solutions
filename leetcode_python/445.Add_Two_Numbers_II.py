# https://leetcode.com/problems/add-two-numbers-ii/
# 设置两个stack存储链表内容

# Time complexity: O(n+m)
# Space complexity: O(n+m)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack1 = []
        stack2 = []
        while l1 is not None:
            stack1.append(l1.val)
            l1 = l1.next
        while l2 is not None:
            stack2.append(l2.val)
            l2 = l2.next

        res_next = None
        carry = 0
        while stack1 or stack2:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            temp = val1 + val2 + carry
            carry, val = divmod(temp, 10)
            res = ListNode(val)
            res.next = res_next
            res_next = res

        if carry > 0:
            res = ListNode(carry)
            res.next = res_next

        return res
