# https://leetcode.com/problems/linked-list-cycle/
# 双指针方法，slow走一步，fast走两步，
# 如果没有循环的话，fast会一直走到重点，不会遇到slow
# 如果有循环的话，fast一定会遇到slow

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
