# https://leetcode.com/problems/linked-list-cycle-ii/
# 比较通俗的解释
# https://www.bilibili.com/video/av48348861/
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break
        else:
            return None

        while head is not slow:
            slow = slow.next
            head = head.next

        return head
