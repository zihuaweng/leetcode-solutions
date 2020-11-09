# https://leetcode.com/problems/reorder-list/
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 找中间点
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 反转后半段
        reverse = None
        while slow:
            temp = slow.next
            slow.next = reverse
            reverse = slow
            slow = temp

        # 间隔插入head链表里面
        res = ListNode(0)
        cur = res
        while reverse and head.next:    # 123->None    543 -> None
            cur.next = head
            head = head.next
            cur.next.next = reverse
            reverse = reverse.next
            cur = cur.next.next

        head = res.next


