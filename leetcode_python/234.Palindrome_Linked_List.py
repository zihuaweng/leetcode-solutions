# https://leetcode.com/problems/palindrome-linked-list/
# 设置前后指针，fast & slow 同时往后走，slow停下来的位置就是列表中间位置
# 反转slow 后面的内容，得到后半部分反转的列表
# 同时遍历head 和反转列表，数值想等就后移，如果最后反转列表为空，返回正。

# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or head.next is None:
            return True
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        p = None
        while slow:
            temp = slow.next
            slow.next = p
            p = slow
            slow = temp

        while p and p.val == head.val:
            p = p.next
            head = head.next

        return p is None
